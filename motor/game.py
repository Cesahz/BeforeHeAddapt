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
            #mostrar estado actual
            self._ui.mostrar_estado(self._jugador,self._enemigo)
            
            #turno del jugador
            #logica del turno del jugador aca luego!!!!!!!!!!!
            
            
            #condicion de victoria
            if not self._enemigo.esta_vivo():
                self._estado = "VICTORIA"
                break
            
            
            #turno del enemigo
            #logica del enemigo y la IA de mahoraga aca luego !!!!!!!!!!
            
            #condicion de derrota
            if not self._jugador.esta_vivo():
                self._estado = "DERROTA"
                break
        #fin
        self._ui.mostrar_log(f"Fin del combate. Resultado: {self._estado}")
            