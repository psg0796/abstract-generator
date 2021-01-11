from typing import Dict
import os
from scipy.io.idl import AttrDict

from input import get_input

default_types = {
    "int": "int",
    "string": "str",
}


class Generator:
    input_dict: Dict

    def __init__(self, input_dict: Dict):
        self.input_dict = input_dict
        self.input_dict = get_input()
        self.output = f"""from typing import *
from abc import ABCMeta, abstractmethod
from enum import Enum

"""

    def generate_method(self, method_name, method_schema, indent):
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

    def generate_class(self, name, obj):
        class_name = name
        methods = obj.methods
        methods_string = ""
        for k, v in methods.items():
            methods_string += self.generate_method(k, v, "\t")
        return f"""
class {class_name}:
\t__metaclass__ = ABCMeta
{methods_string}
"""

    @staticmethod
    def get_string_val(type_, val):
        if type_ == "str":
            return f"\'{val}\'"

    def generate_enum(self, name, obj):
        enum_name = name
        enum_type = default_types.get(obj.type[5: -1])
        members: Dict[str, str] = obj.members
        members_string = ""
        for k, v in members.items():
            members_string += f"""
\t{k}: {enum_type} = {self.get_string_val(enum_type, v)}
"""
        return f"""
class {enum_name}(Enum):
{members_string}
"""

    def generate(self):
        for k, obj in self.input_dict.items():
            obj = AttrDict(obj)
            if obj.type == "class":
                self.output += self.generate_class(k, obj)
            elif obj.type.split("[")[0] == "Enum":
                self.output += self.generate_enum(k, obj)

        f = open("output/tmp.py", "w")
        f.write(self.output)
        f.close()
        os.system("black output")


if __name__ == '__main__':
    Generator({}).generate()
