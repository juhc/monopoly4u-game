from .selling_field import SellingField, AbstractGroup

class CommonField(SellingField):
    def __init__(self, name: str, group: AbstractGroup) -> None:
        super().__init__(name, group)
        
