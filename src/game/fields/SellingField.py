from AbstractField import AbstractField
from Player import Player

class SellingField(AbstractField):
    def __init__(self, name: str, cost: int) -> None:
        super().__init__(name)
        self.__cost = cost
        self.__owner: Player

    @property
    def cost(self) -> int:
        return self.__cost
    
    @property
    def owner(self) -> Player:
        return self.__owner
    
    @owner.setter
    def owner(self, player: Player) -> None:
        self.__owner = player