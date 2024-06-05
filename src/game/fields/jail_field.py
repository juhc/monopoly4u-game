from .abstract_field import AbstractField


class JailField(AbstractField):
    def __init__(self) -> None:
        super().__init__("Тюрьма / Посещение")