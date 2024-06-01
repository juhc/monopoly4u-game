from .selling_field import SellingField
from groups import AbstractGroup


class SpecialField(SellingField):
    def __init__(self, name: str, group: AbstractGroup) -> None:
        super().__init__(name, group)