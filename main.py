from dominio.entidades import Gojo, Mahoraga
from ui.consola import InterfazConsola
from motor.game import BeforeHeAdaptsEngine
from dominio.arsenal import ataques_gojo

def main():
    #iniciar interfaz
    terminal = InterfazConsola()
    
    #instanciar entidades
    jugador = Gojo()
    bestia = Mahoraga()
    
    #aplicar las tecnicas
    for tecnica in ataques_gojo:
        jugador.equipar_tecnica(tecnica)
        
    #ensamblar y encender motor
    sistema = BeforeHeAdaptsEngine(jugador=jugador, enemigo=bestia, interfaz=terminal)
    
    #game loop
    sistema.iniciar()

if __name__ == "__main__":
    main()