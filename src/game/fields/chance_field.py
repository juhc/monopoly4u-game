from .abstract_field import AbstractField


class ChanceField(AbstractField):
    def __init__(self) -> None:
        super().__init__("Шанс")