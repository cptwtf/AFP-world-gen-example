from Factories.AbstractGenerator import AbstractGenerator
from Interfaces.Animal import Animal
from Interfaces.Ground import Ground
from Interfaces.Plant import Plant
from Objects.Ground.Swamp import Swamp
from Objects.Animals.Tiger import Tiger
from Objects.Plants.Vine import Vine


class JungleGenerator(AbstractGenerator):
    def create_plant(self) -> Plant:
        return Vine()

    def create_animal(self) -> Animal:
        return Tiger()

    def create_ground(self) -> Ground:
        return Swamp()
