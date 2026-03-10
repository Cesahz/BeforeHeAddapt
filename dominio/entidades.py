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
    def hp_maximo(self):
        return self._hp_maximo
    
    @property
    def ce_maximo(self):
        return self._ce_maximo
    
    @property
    def tecnicas(self):
        return self._tecnicas
    
    @property
    def ce_actual(self):
        return self._ce_actual
    
    def equipar_tecnica(self, tecnica:Ataque):
        self._tecnicas.append(tecnica)
    
    def gastar_ce(self, costo: int) -> bool:
        """Descuenta energia por ataque, true si tiene suficiente, false si no"""
        if self._ce_actual >= costo:
            self._ce_actual -= costo
            return True
        return False
    
    def recibir_dano(self, ataque:Ataque) -> int:
        self._hp_actual -= ataque.dano_base
        if self._hp_actual < 0:
            self._hp_actual = 0
        return ataque.dano_base

class Gojo(Hechicero):
    def __init__(self):
        super().__init__(nombre="Satoru Gojo", hp_maximo=1000, ce_maximo=4000)
        self._infinito_activo = False
    @property
    def infinito_activo(self):
        return self._infinito_activo
    
    def alternar_infinito(self):
        """Enciende o apaga el infinito"""
        self._infinito_activo = not self._infinito_activo
        return self._infinito_activo
    
    def recibir_dano(self, ataque:Ataque, ignora_infinito: bool = False) -> int:
        if self._infinito_activo and not ignora_infinito:
            return 0
        super().recibir_dano(ataque)
        return ataque.dano_base
    
class MaldicionMenor(EntidadCombate):
    def __init__(self):
        super().__init__(nombre="Maldicion Grado 3", hp_maximo=300)
    
    def recibir_dano(self, ataque: Ataque) -> int:
        self._hp_actual -= ataque.dano_base
        if self._hp_actual < 0:
            self._hp_actual = 0
        return ataque.dano_base

#mahoraga
class Mahoraga(EntidadCombate):
    def __init__(self):
        super().__init__(nombre="General Divino Mahoraga", hp_maximo=1200)
        self._rueda_adaptacion = {}
        self._giros_totales = 0
    
    #getter para que la ui pueda leer adaptaciones
    @property
    def adaptaciones(self):
        return self._rueda_adaptacion
    
    @property
    def giros_totales(self):
        return self._giros_totales
    
    def recibir_dano(self, ataque) -> int:
        mitigacion_total = 0.0
        if ataque.tags:
            suma_mitigacion = 0.0
            for tag in ataque.tags:
                #si no existe se come todo el dmg
                nivel_actual = self._rueda_adaptacion.get(tag,0)
                #por cada giro otorga 25% de resistencia
                mitigacion_tag = min(nivel_actual*0.25, 1.0)
                suma_mitigacion += mitigacion_tag
            #promedio de mitigacion, reduce dmg proporcional a los tags adaptados
            mitigacion_total = suma_mitigacion / len(ataque.tags)
            mitigacion_total = min(mitigacion_total, 1.0) #seguro por si acaso
        #aplicar dmg
        dano_final = int(ataque.dano_base * (1.0 - mitigacion_total))
        self._hp_actual -= dano_final
        if self._hp_actual < 0:
            self._hp_actual = 0
        
        #motor de adaptacion
        if self.esta_vivo() and ataque.tags:
            hubo_giro = False
            for tag in ataque.tags:
                nivel = self._rueda_adaptacion.get(tag,0)
                if nivel < 4:
                    self._rueda_adaptacion[tag] = nivel + 1
                    hubo_giro = True
            
            if hubo_giro:
                self._giros_totales += 1
        
        #retornar dmg
        return dano_final
        
    def adaptar_defensa(self,tag: str) -> bool:
        nivel = self._rueda_adaptacion.get(tag,0)
        if nivel < 4:
            self._rueda_adaptacion[tag] = nivel + 1
            self._giros_totales += 1
            return True
        return False