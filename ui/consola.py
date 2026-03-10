import os

class InterfazConsola:
    def limpiar_pantalla(self):
        os.system("cls")
    
    def mostrar_estado(self,hechicero, enemigo):
        print(f"{hechicero.nombre} HP: {hechicero.hp_actual} \n")
        print(f"{enemigo.nombre} HP: {enemigo.hp_actual}")
        
    def pedir_accion(self, tecnicas_disponibles) -> int:
        pass
    
    def mostrar_log(self, mensaje:str):
        print(f"> {mensaje}")
        