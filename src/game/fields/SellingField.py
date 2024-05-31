from AbstractField import AbstractField

class SellingField(AbstractField):
    def __init__(self, name: str, group: int, cost: int, pledge: int, ransom: int) -> None:
        super().__init__(name)
        self.__group = group
        self.__cost = cost
        self.__pledge = pledge
        self.__ransom = ransom
    
    @property
    def group(self) -> int:
        return self.__group

    @property
    def cost(self) -> int:
        return self.__cost
    
    @property
    def pledge(self) -> int:
        return self.__pledge
    
    @property
    def ransom(self) -> int:
        return self.__ransom