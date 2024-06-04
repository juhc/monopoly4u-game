import random


class Cube:
    def __init__(self) -> None:
        self.__score: int

    def roll(self) -> int:
        self.__score = random.randint(1, 6)
        return self.__score

    @property
    def score(self) -> int:
        if self.__score:
            return self.__score

        return 0


class Dice:
    def __init__(self) -> None:
        self.__score: int
        self.__cubes: list[Cube] = [Cube(), Cube()]

    def roll(self) -> int:
        self.__score = sum([cube.roll() for cube in self.__cubes])
        return self.__score

    def get_cubes(self) -> list[int]:
        return [cube.score for cube in self.__cubes]

    @property
    def is_double(self) -> bool:
        cubes_scores = self.get_cubes()
        return all([cube == cubes_scores[0] for cube in cubes_scores])
