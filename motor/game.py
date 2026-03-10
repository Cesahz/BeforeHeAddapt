from dominio.ataques import Ataque
from motor.persistencia import GestorGuardado
import random
import os

class BeforeHeAdaptsEngine:
    def __init__(self,jugador,enemigo,interfaz):
        self._jugador = jugador
        self._enemigo = enemigo
        self._ui = interfaz
        self._estado = "Activo"
        self._turnos_aturdido = 0
        self._gestor = GestorGuardado()
        
    def iniciar(self):
        self._ui.limpiar_pantalla()
        self._ui.mostrar_log("Iniciando Combate. . .")
        
        if os.path.exists(self._gestor.archivo):
            if self._ui.preguntar_carga():
                self._gestor.cargar(self._jugador, self._enemigo)
                self._ui.mostrar_log("Simulación restaurada con éxito.")
            else:
                self._gestor.borrar()
        
        while self._estado == "Activo":
            self._ui.limpiar_pantalla()
            self._ui.mostrar_estado(self._jugador,self._enemigo)
            self._jugador.recuperar_ce(50)
            
            #turno del jugador
            self._ui.mostrar_log(f"Turno de {self._jugador.nombre}")
            accion = self._ui.pedir_accion(self._jugador)
            
            if hasattr(self._jugador, 'infinito_activo') and self._jugador.infinito_activo:
                if self._jugador.gastar_ce(150):
                    self._ui.mostrar_log("🌀 El Infinito consume 150 CE para mantenerse activo.")
                else:
                    self._jugador.alternar_infinito()
                    self._ui.mostrar_log("⚠️ Te has quedado sin energía. El Infinito colapsa.")

            if accion == "INFINITO":
                estado_infinito = self._jugador.alternar_infinito()
                txt = "ENCENDIDO" if estado_infinito else "APAGADO"
                self._ui.mostrar_log(f"> Has {txt} el Infinito. El espacio se distorsiona a tu alrededor.")
                continue #no gasta turno
            else:
                ataque_elegido = self._jugador.tecnicas[accion]
                if self._jugador.gastar_ce(ataque_elegido.costo_ce):
                    #logica de dominio
                    if "Dominio" in ataque_elegido.tags:
                        self._ui.mostrar_log("🤞 Expansión de Dominio: Vacío Inconmensurable.")
                        self._ui.mostrar_log("> La mente de Mahoraga es inundada con información infinita...")
                        self._turnos_aturdido = 2 #paralizado por 2 turnos
                        if hasattr(self._enemigo, 'sufrir_vacio'):
                            self._enemigo.sufrir_vacio() #pierde su adaptacion
                        continue
                    multiplicador = 1.0
                    es_black_flash = False
                    ataques_compatibles = ["Golpe Reforzado", "Golpe Blue","Golpe Basico"]
                    
                    # black flash 
                    if ataque_elegido.nombre in ataques_compatibles and random.randint(1,100) <= 10:
                        multiplicador = 2.5
                        es_black_flash = True
                        self._jugador.recuperar_ce(200)
                    
                    dano_calculado = int(ataque_elegido.dano_base * multiplicador)
                    ataque_temporal = Ataque(
                        nombre=ataque_elegido.nombre,
                        costo_ce=ataque_elegido.costo_ce,
                        dano_base=dano_calculado,
                        tags=ataque_elegido.tags
                    )
                    
                    dano_causado = self._enemigo.recibir_dano(ataque_temporal)

                    if es_black_flash:
                        self._ui.mostrar_log("¡DESTELLO NEGRO! Golpe critico...")
                        self._ui.mostrar_log(f"¡Usaste {ataque_elegido.nombre}! Causaste {dano_causado} de daño CRÍTICO.")
                    else:
                        self._ui.mostrar_log(f"¡Usaste {ataque_elegido.nombre}! Causaste {dano_causado} de daño.")
                else:
                    self._ui.mostrar_log("> No tienes suficiente Energía Maldita. Pierdes el turno por ineficiencia.")
                
            if not self._enemigo.esta_vivo:
                self._estado = "VICTORIA"
                break
            
            # turno del enemigo
            if self._turnos_aturdido > 0:
                self._ui.mostrar_log(f"Turno de {self._enemigo.nombre}")
                self._ui.mostrar_log("> 🧠 Mahoraga está paralizado procesando el Vacío...")
                self._turnos_aturdido -= 1
                continue #saltar turno
            
            self._ui.mostrar_log(f"Turno de {self._enemigo.nombre}")
            ataque_enemigo = Ataque(nombre="Golpe Físico Crudo", costo_ce=0, dano_base=85, tags=["Golpe"])
            ignora_infinito = False
            
            # verificar la adaptacion del infinito
            if hasattr(self._enemigo, 'adaptaciones') and self._enemigo.adaptaciones.get("Infinito", 0) >= 4:
                ignora_infinito = True
                ataque_enemigo.nombre = "Corte que Divide el Mundo"
                ataque_enemigo.dano_base = 250 
            
            # procesar dmg contra el jugador 
            bloqueado = False
            if hasattr(self._jugador, 'infinito_activo'):
                dano_recibido = self._jugador.recibir_dano(ataque_enemigo, ignora_infinito)
                bloqueado = (dano_recibido == 0 and self._jugador.infinito_activo)
            else:
                dano_recibido = self._jugador.recibir_dano(ataque_enemigo)
            
            if bloqueado:
                self._ui.mostrar_log(f"> El {ataque_enemigo.nombre} de {self._enemigo.nombre} se detuvo inexplicablemente en el aire.")
                # forzar adaptacion de mahoraga
                if hasattr(self._enemigo, 'adaptar_defensa') and self._enemigo.adaptar_defensa("Infinito"):
                    self._ui.mostrar_log("  [SISTEMA] *CLACK* La rueda gira. Mahoraga analiza el espacio a tu alrededor...")
            else:
                self._ui.mostrar_log(f"{self._enemigo.nombre} contraatacó con {ataque_enemigo.nombre} y te causó {dano_recibido} de daño.")
            
            #autoguardado silencioso
            if self._estado == "Activo":
                self._gestor.guardar(self._jugador, self._enemigo)
                
            if not self._jugador.esta_vivo:
                self._estado = "DERROTA"
                break
                
        #fin
        self._gestor.borrar()
        self._ui.limpiar_pantalla()
        self._ui.mostrar_estado(self._jugador, self._enemigo)
        mensaje_final = "Exorcismo completado." if self._estado == "VICTORIA" else "Te has convertido en una maldición..."
        self._ui.mostrar_log(f"Fin del combate. Resultado: {self._estado} - {mensaje_final}")