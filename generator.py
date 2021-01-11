from typing import Dict
from abc import ABCMeta, abstractmethod


class Generator:

    __metaclass__ = ABCMeta

    @abstractmethod
    def generate_method(self, method_name, method_schema, indent) -> str:
        """
        A method to generate the method template from the method schema
        :param method_name: Name of the method
        :param method_schema: schema of the method, contains params and return type
        :param indent: basic indentation to file while generating template
        :return: string format template of generated method
        """

    @abstractmethod
    def generate_class(self, class_name, class_schema, indent) -> str:
        """
        A method to generate the class template from the class schema
        :param class_name: Name of the class
        :param class_schema: Schema of the class, consists of methods which are defined
        :param indent: basic indentation to follow while writing the template
        :return: string format of the generated class
        """
        pass

    @abstractmethod
    def get_string_val(self, type_, val) -> str:
        """
        A method to return the string formatted value
        ex. if called with type_ = str and val = my_string, it returns "my_string",
        so that this can be written as a string in the generated template
        :param type_: type of the val, may be str, int, float, or any basic type
        :param val: value to be converted to the format
        :return: return string formatted value
        """
        pass

    @abstractmethod
    def generate_enum(self, enum_name, enum_schema, indent) -> str:
        """
        A method to generate enum classes
        :param enum_name: Name of the enum
        :param enum_schema: schema of the enum, consists of members and their types
        :param indent: basic indentation to follow while generating the template
        :return: string format of the generated enum class
        """
        pass

    @abstractmethod
    def generate(self) -> None:
        """
        The driver method for the generation of the template in a language
        :return: None
        """
        pass
