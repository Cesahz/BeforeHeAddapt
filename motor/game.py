from dominio.ataques import Ataque

class BeforeHeAdaptsEngine:
    def __init__(self,jugador,enemigo,interfaz):
        self._jugador = jugador
        self._enemigo = enemigo
        self._ui = interfaz
        self._estado = "Activo" #sistema de estados
        
    def iniciar(self):
        self._ui.limpiar_pantalla()
        self._ui.mostrar_log("Iniciando Combate. . .")
        
        #game loop
        while self._estado == "Activo":
            self._ui.limpiar_pantalla()
            #mostrar estado actual
            self._ui.mostrar_estado(self._jugador,self._enemigo)
            
            #turno del jugador
            self._ui.mostrar_log(f"Turno de {self._jugador.nombre}")
            indice_accion = self._ui.pedir_accion(self._jugador.tecnicas)
            ataque_elegido = self._jugador.tecnicas[indice_accion]
            #si tiene CE ataca
            if self._jugador.gastar_ce(ataque_elegido.costo_ce):
                dano_causado = self._enemigo.recibir_dano(ataque_elegido)
                self._ui.mostrar_log(f"¡Usaste {ataque_elegido.nombre}! Causaste {dano_causado} de daño.")
            else:
                self._ui.mostrar_log("> No tienes suficiente Energía Maldita. Pierdes el turno por ineficiencia.")
                
            #condicion de victoria
            if not self._enemigo.esta_vivo():
                self._estado = "VICTORIA"
                break
            
            
            #turno del enemigo
            self._ui.mostrar_log(f"Turno de {self._enemigo.nombre}")
            #Unico golpe temporalmente
            ataque_enemigo = Ataque(nombre="Golpe Físico Crudo", costo_ce=0, dano_base=85, tags=["Golpe"])
            dano_recibido = self._jugador.recibir_dano(ataque_enemigo)
            self._ui.mostrar_log(f"{self._enemigo.nombre} contraatacó con {ataque_enemigo.nombre} y te causó {dano_recibido} de daño.")
            
            #condicion de derrota
            if not self._jugador.esta_vivo():
                self._estado = "DERROTA"
                break
        #fin
        self._ui.limpiar_pantalla()
        self._ui.mostrar_estado(self._jugador, self._enemigo)
        mensaje_final = "Exorcismo completado." if self._estado == "VICTORIA" else "Te has convertido en una maldición..."
        self._ui.mostrar_log(f"Fin del combate. Resultado: {self._estado} - {mensaje_final}")
            