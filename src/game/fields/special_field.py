from .selling_field import SellingField


class SpecialField(SellingField):
    def __init__(self, name: str) -> None:
        super().__init__(name)