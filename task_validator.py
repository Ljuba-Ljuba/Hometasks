from abc import ABCMeta, abstractmethod
import time
import os

class ValidatorException(Exception):
    pass


class Validator(metaclass=ABCMeta):
    types = {}

    # def __init__(self, name):
    #     self.name = name

    @abstractmethod
    def validate(self):
        pass


    @classmethod
    def add_type(cls, name, klass):
        """кладем в словарь пару из названия типа и соответствующего обработчика """
        if not name:
            raise ValidatorException('Type must have a name!')
        if not issubclass(klass, Validator):
            raise ValidatorException(
            'Class "{}" is not Validator!'.format(klass)
            )
        cls.types[name] = klass


    @classmethod
    def get_instance(cls, name, *args, **kwargs):
        """вызываем необходимый обработчик, который оказался в имени класс"""
    # Шаблон "Factory Method"
        klass = cls.types.get(name)

        if klass is None:
            raise ValidatorException(
            'Type "{}" not found!'.format(name)
            )

        return klass()

class EMailValidator(Validator):

    def validate(self, value):
        if value.count('@') != 1:
            return False
        if value.count('.') == 0:
            return False
        return True


class DateTimeValidator(Validator):

    def validate(self, value):
        good_value = [
            '%Y-%m-%d',
            '%Y-%m-%d %H:%M',
            '%Y-%m-%d %H:%M:%S',
            '%d.%m.%Y',
            '%d.%m.%Y %H:%M',
            '%d.%m.%Y %H:%M:%S',
            '%d/%m/%Y',
            '%d/%m/%Y %H:%M',
            '%d/%m/%Y %H:%M:%S']


        for data in good_value:
            try:
                time.strptime(value, data)
                return True
            except ValueError:
                continue

        return False


Validator.add_type('email',EMailValidator)
Validator.add_type('date', DateTimeValidator)
