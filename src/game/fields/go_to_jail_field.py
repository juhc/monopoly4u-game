from .abstract_field import AbstractField


class GoToJailField(AbstractField):
    def __init__(self) -> None:
        super().__init__("Отправляйтесь в тюрьму")