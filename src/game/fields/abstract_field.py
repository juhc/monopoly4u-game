from abc import ABC


class AbstractField(ABC):
    def __init__(self, name: str) -> None:
        self.__name = name
    
    @property
    def name(self) -> str:
        return self.__name
    
    def model_dump(self) -> dict:
        return {"name": self.name}