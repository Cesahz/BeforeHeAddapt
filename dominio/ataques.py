#definir estructura de tecnicas
class Ataque:
    """
    Representa una tecnica o ataque fisico
    """
    def __init__(self,nombre: str, costo_ce: int, dano_base: int, tags: list):
        self.nombre = nombre
        self.costo_ce = costo_ce
        self.dano_base = dano_base
        self.tags = tags #categorias para la adaptacion