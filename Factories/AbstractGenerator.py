from __future__ import annotations
from abc import ABC, abstractmethod

from Interfaces.Animal import Animal
from Interfaces.Ground import Ground
from Interfaces.Plant import Plant


class AbstractGenerator(ABC):
    @abstractmethod
    def create_plant(self) -> Plant:
        pass

    @abstractmethod
    def create_animal(self) -> Animal:
        pass

    @abstractmethod
    def create_ground(self) -> Ground:
        pass
