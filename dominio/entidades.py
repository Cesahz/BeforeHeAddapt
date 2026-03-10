from abc import ABC, abstractmethod
from dominio.ataques import Ataque

#la clase base
class EntidadCombate(ABC):
    def __init__(self, nombre:str, hp_maximo: int):
        self._nombre = nombre
        self._hp_maximo = hp_maximo
        self._hp_actual = hp_maximo
        
    #getters para leer el estado sin modificar
    @property
    def nombre(self):
        return self._nombre
    @property
    def hp_actual(self):
        return self._hp_actual
    @property
    def esta_vivo(self) -> bool:
        return self._hp_actual > 0
    
    #polimorfismo, metodo que obliga a definir a los hijos como recibir dmg
    @abstractmethod
    def recibir_dano(self, ataque: Ataque):
        pass

#herencias
class Hechicero(EntidadCombate):
    def __init__(self, nombre:str,hp_maximo:int,ce_maximo:int):
        super().__init__(nombre, hp_maximo)
        self._ce_maximo = ce_maximo
        self._ce_actual = ce_maximo
        self._tecnicas = [] #lista de objetos ataque
    
    #getters para la Ui
    @property
    def tecnicas(self):
        return self._tecnicas
    
    @property
    def ce_actual(self):
        return self._ce_actual
    
    def equipar_tecnica(self, tecnica:Ataque):
        self._tecnicas.append(tecnica)
    
    def recibir_dano(self, ataque:Ataque):
        self._hp_actual -= ataque.dano_base
        if self._hp_actual < 0:
            self._hp_actual = 0

class MaldicionMenor(EntidadCombate):
    def __init__(self):
        super().__init__(nombre="Maldicion Grado 3", hp_maximo=300)
    
    def recibir_dano(self, ataque: Ataque):
        self._hp_actual -= ataque.dano_base
        if self._hp_actual < 0:
            self._hp_actual = 0

#mahoraga
class Mahoraga(EntidadCombate):
    def __init__(self):
        super().__init__(nombre="General Divino Mahoraga", hp_maximo=1200)
        self._rueda_adaptacion = {}
    
    def recibir_dano(self, ataque):
        dano_final = ataque.dano_base
        
        #analizar ataque recibido
        for tag in ataque.tags:
            if tag in self._rueda_adaptacion:
                #si el tag esta en la rueda, sigue adaptando o anula el dano
                break
    
        #recibir impacto
        self._hp_actual -= dano_final
        if self._hp_actual < 0:
            self._hp_actual = 0
        
        #girar la rueda
        if dano_final > 0:
            for tag in ataque.tags:
                self._rueda_adaptacion[tag] = True