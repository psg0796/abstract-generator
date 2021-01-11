from typing import Dict
import os
from scipy.io.idl import AttrDict
from generator import Generator

from input import get_input

default_types = {
    "int": "int",
    "string": "str",
}


class PythonGenerator(Generator):
    input_dict: Dict

    def __init__(self, input_dict: Dict):
        self.input_dict = input_dict
        self.input_dict = get_input()
        self.output = f"""from typing import *
from abc import ABCMeta, abstractmethod
from enum import Enum

"""

    def generate_method(self, method_name, method_schema, indent) -> str:
        params = method_schema.get("params")
        returns = method_schema.get("returns", "None")
        param_string = "self"
        if params:
            for k, v in params.items():
                param_string += f", {k}: {default_types.get(v, v)}"
        return f"""
{indent}@abstractmethod
{indent}def {method_name}({param_string}) -> {default_types.get(returns, returns)}:
{indent}\tpass
"""

    def generate_class(self, class_name, class_schema, indent) -> str:
        class_name = class_name
        methods = class_schema.methods
        methods_string = ""
        for k, v in methods.items():
            methods_string += self.generate_method(k, v, f"{indent}\t")
        return f"""
{indent}class {class_name}:
{indent}\t__metaclass__ = ABCMeta
{methods_string}
"""

    def get_string_val(self, type_, val) -> str:
        if type_ == "str":
            return f"\'{val}\'"

    def generate_enum(self, enum_name, enum_schema, indent) -> str:
        enum_name = enum_name
        enum_type = default_types.get(enum_schema.type[5: -1])
        members: Dict[str, str] = enum_schema.members
        members_string = ""
        for k, v in members.items():
            members_string += f"""
{indent}\t{k}: {enum_type} = {self.get_string_val(enum_type, v)}
"""
        return f"""
{indent}class {enum_name}(Enum):
{indent}{members_string}
"""

    def generate(self) -> None:
        for k, obj in self.input_dict.items():
            obj = AttrDict(obj)
            if obj.type == "class":
                self.output += self.generate_class(k, obj, "")
            elif obj.type.split("[")[0] == "Enum":
                self.output += self.generate_enum(k, obj, "")

        f = open("output/tmp.py", "w")
        f.write(self.output)
        f.close()
        os.system("black output/*")


if __name__ == '__main__':
    PythonGenerator({}).generate()
