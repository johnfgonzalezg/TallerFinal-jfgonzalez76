from models.domestic_animal import DomesticAnimal
class Dog(DomesticAnimal):
    # Se define el constructor con las variables privadas
    def __init__(self, name: str, weight: float, age: int) -> None:
        super().__init__(name, weight, age)


    # Otros métodos
    @staticmethod
    def make_sound() -> str:
        return '¡Guau, Guau!'
