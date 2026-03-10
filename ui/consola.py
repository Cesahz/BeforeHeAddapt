import os

class InterfazConsola:
    def limpiar_pantalla(self):
        os.system("cls" if os.name == "nt" else "clear")
    
    def mostrar_estado(self,hechicero, enemigo):
        print("=" * 40)
        print(f"🧙‍♂️ {hechicero.nombre}")
        print(f"   HP: {hechicero.hp_actual}/{hechicero.hp_maximo} | CE: {hechicero.ce_actual}/{hechicero.ce_maximo}")
        print("-" * 40)
        print(f"👹 {enemigo.nombre}")
        print(f"   HP: {enemigo.hp_actual}")
        print("=" * 40)
        
        
    def pedir_accion(self, hechicero) -> int | str:
        print("\n¿Qué acción tomarás?")
        tiene_infinito = hasattr(hechicero, 'alternar_infinito')
        if tiene_infinito:
            estado = "ON" if hechicero.infinito_activo else "OFF"
            print(f"[0] 🛡️  Alternar Infinito (Estado actual: {estado})")
        for i, tecnica in enumerate(hechicero.tecnicas):
            print(f"[{i + 1}] {tecnica.nombre} (Costo CE: {tecnica.costo_ce} | Daño: {tecnica.dano_base})")
            
        while True:
            try:
                opcion = input("\nIngresa tu elección: ")
                if opcion == "0" and tiene_infinito:
                    return "INFINITO"
                indice = int(opcion) - 1
                
                if 0 <= indice < len(hechicero.tecnicas):
                    return indice
                else:
                    print("> Error: Elige un número válido de la lista.")
            except ValueError:
                print("> Error: Por favor, ingresa solo números.")
        
    
    def mostrar_log(self, mensaje:str):
        print(f"> {mensaje}")
        input("  [Presiona Enter para continuar...]")