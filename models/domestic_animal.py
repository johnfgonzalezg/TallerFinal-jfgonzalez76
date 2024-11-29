from models.animal import Animal

class DomesticAnimal(Animal):
    def __init__(self, name: str, weight: float, age: int) -> None:
        super().__init__(name, weight, age)
        self._kilos_eaten = 0
    
    def eat(self, kilos: float):
        if isinstance(kilos, float):
            self._kilos_eaten += (kilos * 0.8)
        else:
            raise ValueError('El valor debe ser un flotante.')
    
    def get_kilos_eaten(self) -> float:
        return self._kilos_eaten