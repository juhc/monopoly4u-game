from SellingField import SellingField

class CommonField(SellingField):
    def __init__(self,
                 name: str,
                 group: int,
                 cost: int,
                 pledge: int,
                 ransom: int,
                 branch: int,
                 basic_rent: int,
                 monopoly_rent: int,
                 one_house_rent: int,
                 two_houses_rent: int,
                 three_houses_rent: int,
                 four_houses_rent: int,
                 hotel_rent: int) -> None:
        super().__init__(name, group, cost, pledge, ransom)
        self.__branch = branch
        self.__basic_rent = basic_rent
        self.__monopoly_rent = monopoly_rent
        self.__one_house_rent = one_house_rent
        self.__two_houses_rent = two_houses_rent
        self.__three_houses_rent = three_houses_rent
        self.__four_houses_rent = four_houses_rent
        self.__hotel_rent = hotel_rent