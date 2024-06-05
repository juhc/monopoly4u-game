from groups import CommonGroup, SpecialGroup
from fields import CommonField, SpecialField, ChanceField, TaxField, StartField, JailField, JackpotField, GoToJailField
from pathlib import Path
from typing import TYPE_CHECKING
import yaml
if TYPE_CHECKING:
    from groups import AbstractGroup
    from fields import AbstractField


types_dict = {
    "CommonField": CommonField,
    "SpecialField": SpecialField,
    "ChanceField": ChanceField,
    "TaxField": TaxField,
    "StartField": StartField,
    "JailField": JailField,
    "JackpotField": JackpotField,
    "GoToJailField": GoToJailField,
    "CommonGroup": CommonGroup,
    "SpecialGroup": SpecialGroup
}

class FieldsBuilder:
    def __init__(self) -> None:
        self.__groups: list["AbstractGroup"] = []
        self.__fields: list["AbstractField"] = []
        
        with open(Path(__file__).parent / "yamls" / "groups.yml", encoding="utf-8") as f:
            raw_groups: list[dict] = yaml.safe_load(f)

        with open(Path(__file__).parent / "yamls" / "fields.yml", encoding="utf-8") as f:
            raw_fields: list[dict] = yaml.safe_load(f)

        for group_args in raw_groups:
            group_type = types_dict[group_args.pop("type")]
            self.__groups.append(group_type(**group_args))

        for field_args in raw_fields:
            field_type = types_dict[field_args.pop("type")]
            group_index = field_args.pop("group", None)
            
            field = field_type(**field_args)

            self.__fields.append(field)

            if group_index is not None:
                field.group = self.__groups[group_index]
                self.__groups[group_index].fields.append(field)
    
    @property
    def fields(self) -> list["AbstractField"]:
        return self.__fields