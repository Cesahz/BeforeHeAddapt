import os
import time

class InterfazConsola:
    def __init__(self):
        self.registro_eventos = []

    def limpiar_pantalla(self):
        os.system("cls" if os.name == "nt" else "clear")

    def _crear_barra(self, actual, maximo, longitud=20):
        # Optimizado en 2 líneas eliminando variables intermedias innecesarias
        llenos = int(longitud * (max(0, actual) / maximo))
        return f"[{'█' * llenos}{'-' * (longitud - llenos)}]"

    def mostrar_estado(self, hechicero, enemigo):
        # 1. Pre-calculamos las variables complejas
        hp_e = f"{self._crear_barra(enemigo.hp_actual, enemigo.hp_maximo)} {enemigo.hp_actual}/{enemigo.hp_maximo}"
        hp_h = f"{self._crear_barra(hechicero.hp_actual, hechicero.hp_maximo)} {hechicero.hp_actual}/{hechicero.hp_maximo}"
        ce_h = f"{self._crear_barra(hechicero.ce_actual, hechicero.ce_maximo)} {hechicero.ce_actual}/{hechicero.ce_maximo}"
        
        # 2. Formateo condicional de adaptaciones limpio
        adaptaciones = ""
        if hasattr(enemigo, 'adaptaciones') and enemigo.adaptaciones:
            adaps_activas = ", ".join([f"{k.upper()}: Nivel {v}" for k, v in enemigo.adaptaciones.items() if v > 0])
            if adaps_activas: 
                adaptaciones = f"\n   ⚙️ ADAPTACIONES: {adaps_activas}"

        # 3. El uso pragmático de un string multi-línea (f-string triple)
        print(f"""{"=" * 50}
👹 ENEMIGO: {enemigo.nombre}
   HP: {hp_e}{adaptaciones}
{"-" * 50}
🧙‍♂️ JUGADOR: {hechicero.nombre}
   HP: {hp_h}
   CE: {ce_h}
{"=" * 50}\n""")

        # Volcado del log
        for evento in self.registro_eventos:
            time.sleep(0.3)
            print(evento)
        print()
        self.registro_eventos.clear()

    def pedir_accion(self, hechicero) -> int | str:
        print("--- TUS TÉCNICAS ---")
        tiene_infinito = hasattr(hechicero, 'alternar_infinito')
        
        # Condicional en una sola línea (Operador Ternario)
        if tiene_infinito:
            print(f" [0] Alternar Infinito (Estado: {'ON' if hechicero.infinito_activo else 'OFF'})")

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