from Factories.AbstractGenerator import AbstractGenerator
from Interfaces.Animal import Animal
from Interfaces.Ground import Ground
from Interfaces.Plant import Plant
from Objects.Ground.Concrete import Concrete
from Objects.Animals.Hoomin import Hoomin
from Objects.Plants.StreetLamp import StreetLamp


class CityGenerator(AbstractGenerator):
    def create_plant(self) -> Plant:
        return StreetLamp()

    def create_animal(self) -> Animal:
        return Hoomin()

    def create_ground(self) -> Ground:
        return Concrete()
