import os

class InterfazConsola:
    def limpiar_pantalla(self):
        os.system("cls" if os.name == "nt" else "clear")
    
    def mostrar_estado(self,hechicero, enemigo):
        print("=" * 40)
        print(f"🧙‍♂️ {hechicero.nombre}")
        print(f"   HP: {hechicero.hp_actual}/{hechicero._hp_maximo} | CE: {hechicero.ce_actual}/{hechicero._ce_maximo}")
        print("-" * 40)
        print(f"👹 {enemigo.nombre}")
        print(f"   HP: {enemigo.hp_actual}")
        print("=" * 40)
        
        
    def pedir_accion(self, tecnicas_disponibles) -> int:
        print("\n¿Qué técnica maldita utilizarás?")
        for i, tecnica in enumerate(tecnicas_disponibles):
            print(f"[{i + 1}] {tecnica.nombre} (Costo CE: {tecnica.costo_ce} | Daño: {tecnica.dano_base})")
            while True:
                try:
                    opcion = input("\nIngresa el número de la técnica: ")
                    indice = int(opcion) - 1
                    if 0 <= indice < len(tecnicas_disponibles):
                        return indice
                    else:
                        print(">Error: Elige un número válido de la lista.")
                except ValueError:
                    print(">Error: Por favor, ingresa solo números.")
        
    
    def mostrar_log(self, mensaje:str):
        print(f"> {mensaje}")
        input("  [Presiona Enter para continuar...]")