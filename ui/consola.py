import os
import time

# Paleta de colores ANSI
class Colores:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    RED = '\033[31m'

class InterfazConsola:
    def __init__(self):
        # Almacenamos los mensajes del turno actual para imprimirlos todos juntos
        self.registro_eventos = []

    def limpiar_pantalla(self):
        os.system("cls" if os.name == "nt" else "clear")
    
    def _crear_barra(self, actual, maximo, longitud=20, color_lleno=Colores.GREEN, color_vacio=Colores.ENDC):
        """Genera una barra visual estilo [██████      ]"""
        porcentaje = actual / maximo
        bloques_llenos = int(longitud * porcentaje)
        bloques_vacios = longitud - bloques_llenos
        barra = f"{color_lleno}{'█' * bloques_llenos}{Colores.ENDC}{color_vacio}{'-' * bloques_vacios}{Colores.ENDC}"
        return barra

    def mostrar_estado(self, hechicero, enemigo):
        """Dibuja el tablero principal del combate con barras visuales"""
        print(f"{Colores.BOLD}{Colores.CYAN}{'=' * 50}{Colores.ENDC}")
        
        # --- ZONA DEL ENEMIGO ---
        barra_hp_enemigo = self._crear_barra(enemigo.hp_actual, enemigo.hp_maximo, color_lleno=Colores.FAIL)
        print(f"👹 {Colores.BOLD}{Colores.WARNING}{enemigo.nombre}{Colores.ENDC}")
        print(f"   HP: [{barra_hp_enemigo}] {enemigo.hp_actual}/{enemigo.hp_maximo}")
        
        # Mostrar las adaptaciones de Mahoraga si existen y son mayores a 0
        if hasattr(enemigo, 'adaptaciones'):
            adaptaciones_activas = {k: v for k, v in enemigo.adaptaciones.items() if v > 0}
            if adaptaciones_activas:
                str_adaptaciones = ", ".join([f"{k.upper()}: Nivel {v}" for k, v in adaptaciones_activas.items()])
                print(f"   ⚙️  Adaptaciones: {Colores.HEADER}{str_adaptaciones}{Colores.ENDC}")
        
        print(f"{Colores.CYAN}{'-' * 50}{Colores.ENDC}")
        
        # --- ZONA DEL JUGADOR ---
        barra_hp_jugador = self._crear_barra(hechicero.hp_actual, hechicero.hp_maximo)
        barra_ce_jugador = self._crear_barra(hechicero.ce_actual, hechicero.ce_maximo, color_lleno=Colores.BLUE)
        
        print(f"🧙‍♂️ {Colores.BOLD}{Colores.GREEN}{hechicero.nombre}{Colores.ENDC}")
        print(f"   HP: [{barra_hp_jugador}] {hechicero.hp_actual}/{hechicero.hp_maximo}")
        print(f"   CE: [{barra_ce_jugador}] {hechicero.ce_actual}/{hechicero.ce_maximo}")
        
        print(f"{Colores.BOLD}{Colores.CYAN}{'=' * 50}{Colores.ENDC}\n")

        # --- IMPRESIÓN DEL LOG ---
        # Imprime todos los eventos ocurridos desde la última vez que se limpió la pantalla
        if self.registro_eventos:
            for evento in self.registro_eventos:
                # Agregar un pequeño delay artificial para el Game Feel (opcional)
                time.sleep(0.3) 
                print(f" {evento}")
            print("\n")
            self.registro_eventos.clear() # Limpia el registro para el siguiente turno

    def pedir_accion(self, hechicero) -> int | str:
        """Menú de acciones más compacto y legible"""
        print(f"{Colores.BOLD}--- ACCIONES DISPONIBLES ---{Colores.ENDC}")
        tiene_infinito = hasattr(hechicero, 'alternar_infinito')
        
        if tiene_infinito:
            estado = f"{Colores.BLUE}ON{Colores.ENDC}" if hechicero.infinito_activo else f"{Colores.ENDC}OFF"
            print(f"  [0] 🛡️  Alternar Infinito (Estado: {estado})")
            
        for i, tecnica in enumerate(hechicero.tecnicas):
            # Colorear el Púrpura o el Dominio para que destaquen
            color_tecnica = Colores.PURPLE if "Purple" in tecnica.nombre or "Void" in tecnica.nombre else Colores.ENDC
            print(f"  [{i + 1}] {color_tecnica}{tecnica.nombre}{Colores.ENDC} (CE: {tecnica.costo_ce} | Daño: {tecnica.dano_base})")
            
        while True:
            try:
                print(f"\n{Colores.BOLD}Tu elección >> {Colores.ENDC}", end="")
                opcion = input()
                
                if opcion == "0" and tiene_infinito:
                    return "INFINITO"
                
                indice = int(opcion) - 1
                if 0 <= indice < len(hechicero.tecnicas):
                    return indice
                else:
                    self._imprimir_error("Elige un número de la lista.")
            except ValueError:
                self._imprimir_error("Por favor, ingresa solo números.")

    def mostrar_log(self, mensaje: str):
        """En lugar de imprimir y pausar, acumula el mensaje para mostrarlo en bloque."""
        # Colorear partes clave del mensaje automáticamente
        if "DESTELLO NEGRO" in mensaje:
            mensaje = f"{Colores.RED}{Colores.BOLD}{mensaje}{Colores.ENDC}"
        elif "*CLACK*" in mensaje:
            mensaje = f"{Colores.WARNING}{mensaje}{Colores.ENDC}"
        elif "DERROTA" in mensaje:
            mensaje = f"{Colores.FAIL}{Colores.BOLD}{mensaje}{Colores.ENDC}"
        elif "VICTORIA" in mensaje:
            mensaje = f"{Colores.GREEN}{Colores.BOLD}{mensaje}{Colores.ENDC}"
            
        self.registro_eventos.append(f"> {mensaje}")
        
    def _imprimir_error(self, mensaje):
        """Utilidad interna para errores de input"""
        print(f"  {Colores.FAIL}❌ {mensaje}{Colores.ENDC}")