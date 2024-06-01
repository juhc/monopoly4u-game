from groups import AbstractGroup, CommonGroup, SpecialGroup
from fields import AbstractField, SellingField, CommonField, SpecialField, ChanceField, TaxField, StartField, JailField, JackpotField, GoToJailField
from pathlib import Path
import yaml


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
        with open(Path(__file__).parent / "yamls" / "groups.yml", encoding="utf-8") as f:
            raw_groups: list[dict] = yaml.safe_load(f)

        with open(Path(__file__).parent / "yamls" / "fields.yml", encoding="utf-8") as f:
            raw_fields: list[dict] = yaml.safe_load(f)

        self.__fields: list[AbstractField] = []
        self.__groups: list[AbstractGroup] = []

        for group_args in raw_groups:
            group_type = types_dict[group_args["type"]]
            group_args.pop("type", None)
            self.__groups.append(group_type(**group_args))

        for field_args in raw_fields:
            field_type = types_dict[field_args["type"]]
            field_args.pop("type", None)
            group_index = field_args.get("group")
            
            if group_index is not None:
                field_args["group"] = self.__groups[group_index]
            
            self.__fields.append(field_type(**field_args))
            
            if group_index is not None:
                self.__groups[group_index].fields.append(self.__fields[-1])
    
    @property
    def fields(self) -> list[AbstractField]:
        return self.__fields