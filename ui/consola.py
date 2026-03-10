import os
import time

class InterfazConsola:
    def __init__(self):
        self.registro_eventos = []

    def limpiar_pantalla(self):
        os.system("cls" if os.name == "nt" else "clear")

    def _crear_barra(self, actual, maximo, longitud=20):
        # crear barras de vida proporcional a la vida
        vida_real = max(0, actual) # Evita que la barra intente dibujar valores negativos
        llenos = int(longitud * (vida_real / maximo))
        vacios = longitud - llenos
        return f"[{'█' * llenos}{'-' * vacios}]"

    def mostrar_estado(self, hechicero, enemigo):
        # calculo de variables complejas
        hp_e = f"{self._crear_barra(enemigo.hp_actual, enemigo.hp_maximo)} {enemigo.hp_actual}/{enemigo.hp_maximo}"
        hp_h = f"{self._crear_barra(hechicero.hp_actual, hechicero.hp_maximo)} {hechicero.hp_actual}/{hechicero.hp_maximo}"
        ce_h = f"{self._crear_barra(hechicero.ce_actual, hechicero.ce_maximo)} {hechicero.ce_actual}/{hechicero.ce_maximo}"
        
        # progreso de adaptacion (Bucle tradicional, imposible de malinterpretar)
        texto_adaptaciones = ""
        if hasattr(enemigo, 'adaptaciones') and enemigo.adaptaciones:
            lista_activas = []
            for tag, nivel in enemigo.adaptaciones.items():
                if nivel > 0:
                    lista_activas.append(f"{tag.upper()}: Nivel {nivel}")
            
            if len(lista_activas) > 0: 
                texto_adaptaciones = f"\n   ⚙️ ADAPTACIONES: {', '.join(lista_activas)}"

        # string multi linea en print
        print(f"""{"=" * 50}
👹 ENEMIGO: {enemigo.nombre}
   HP: {hp_e}{texto_adaptaciones}
{"-" * 50}
🧙‍♂️ JUGADOR: {hechicero.nombre}
   HP: {hp_h}
   CE: {ce_h}
{"=" * 50}\n""")

        # volcado de logs
        for evento in self.registro_eventos:
            time.sleep(0.3)
            print(evento)
        print()
        self.registro_eventos.clear()

    def pedir_accion(self, hechicero):
        print("--- TUS TÉCNICAS ---")
        tiene_infinito = hasattr(hechicero, 'alternar_infinito')
        
        # menu de tecnicas (Ternario extraído a una variable para lectura limpia)
        if tiene_infinito:
            estado_infinito = "ON" if hechicero.infinito_activo else "OFF"
            print(f" [0] Alternar Infinito (Estado: {estado_infinito})")

        for i, t in enumerate(hechicero.tecnicas):
            print(f" [{i + 1}] {t.nombre} (Costo: {t.costo_ce} CE | Daño: {t.dano_base})")

        while True:
            opcion = input("\nElige tu acción >> ")
            if opcion == "0" and tiene_infinito: 
                return "INFINITO"
                
            try:
                indice = int(opcion) - 1
                if 0 <= indice < len(hechicero.tecnicas): 
                    return indice
                print("> Error: Número fuera de rango.")
            except ValueError:
                print("> Error: Ingresa solo números.")

    def mostrar_log(self, mensaje: str):
        self.registro_eventos.append(f"> {mensaje}")
    
    def preguntar_carga(self) -> bool:
        print("\n💾 SISTEMA: Archivo de simulación previa detectado.")
        while True:
            opcion = input("   ¿Restaurar combate anterior? (S/N) >> ").upper()
            if opcion == "S": return True
            if opcion == "N": return False
            print("   > Error: Ingresa S o N.")