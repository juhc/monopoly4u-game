from .selling_field import SellingField


class CommonField(SellingField):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.__monopoly_ratio = 1.75
        self.__building_basic_rent_difference = 200
    
    @property
    def __delta(self) -> int:
        return self.basic_rent * 5 - 100
    
    # Базовая аренда
    @property
    def basic_rent(self) -> int:
        if self.group.fields[-1] == self:
            return self.group.field_cost // 10
        else:
            return self.group.field_cost // 10 - 20

    # Базовая аренда с монополией
    @property
    def monopoly_rent(self) -> int:
        return int(self.basic_rent * self.__monopoly_ratio)
    
    # Аренда с одним домом
    @property
    def one_house_rent(self) -> int:
        return self.monopoly_rent * 5
    
    # Аренда с двумя домами
    @property
    def two_houses_rent(self) -> int:
        return self.one_house_rent + int((self.__delta + self.__building_basic_rent_difference) * self.__monopoly_ratio)
    
    # Аренда с тремя домами
    @property
    def three_houses_rent(self) -> int:
        return self.two_houses_rent + int((self.__delta + self.__building_basic_rent_difference * 2) * self.__monopoly_ratio)
    
    # Аренда с четырьмя домами
    @property
    def four_houses_rent(self) -> int:
        return self.three_houses_rent + int((self.__delta + self.__building_basic_rent_difference * 3) * self.__monopoly_ratio)
    
    # Аренда с отелем
    @property
    def hotel_rent(self) -> int:
        return self.four_houses_rent + int((self.__delta + self.__building_basic_rent_difference * 4) * self.__monopoly_ratio)