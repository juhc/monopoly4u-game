from abc import ABC, abstractmethod

class AbstractField(ABC):
    def __init__(self, name: str) -> None:
        self.__name = name
    
    # Название поля
    @property
    def name(self) -> str:
        return self.__name
    
    # Действия при входе на поле
    @abstractmethod
    def on_enter(self, player: Player) -> None:
        pass