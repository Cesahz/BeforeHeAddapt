import json
import os

class GestorGuardado:
    """
    Maneja la serialización del estado del juego a un archivo JSON
    """
    def __init__(self, archivo="savegame.json"):
        self.archivo = archivo

    def guardar(self, jugador, enemigo):
        ##mapear los estados exactos en un diccionario JSON
        estado = {
            "jugador": {
                "hp": jugador.hp_actual,
                "ce": jugador.ce_actual,
                "infinito": jugador.infinito_activo if hasattr(jugador, 'infinito_activo') else False
            },
            "enemigo": {
                "hp": enemigo.hp_actual,
                "adaptaciones": enemigo.adaptaciones if hasattr(enemigo, 'adaptaciones') else {},
                "giros": enemigo.giros_totales if hasattr(enemigo, 'giros_totales') else 0
            }
        }
        with open(self.archivo, 'w') as f:
            json.dump(estado, f, indent=4) #cargar en la memoria en json lejible

    def cargar(self, jugador, enemigo):
        if not os.path.exists(self.archivo):
            return False
        
        with open(self.archivo, 'r') as f:
            estado = json.load(f) #proceso inverso, convierte json en diccionario de python
            
        #inyectar los datos guardados directamente
        jugador._hp_actual = estado["jugador"]["hp"]
        jugador._ce_actual = estado["jugador"]["ce"]
        if hasattr(jugador, '_infinito_activo'):
            jugador._infinito_activo = estado["jugador"]["infinito"]
            
        enemigo._hp_actual = estado["enemigo"]["hp"]
        if hasattr(enemigo, '_rueda_adaptacion'):
            enemigo._rueda_adaptacion = estado["enemigo"]["adaptaciones"]
        if hasattr(enemigo, '_giros_totales'):
            enemigo._giros_totales = estado["enemigo"]["giros"]
        
        return True
        
    def borrar(self):
        """
        Elimina el archivo de guardado al morir o ganar
        """
        if os.path.exists(self.archivo):
            os.remove(self.archivo)