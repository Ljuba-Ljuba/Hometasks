from abc import ABCMeta, abstractmethod
import json
import pickle
import os

# class Foo(metaclass=ABCMeta):
#     pass
class ParamHandlerException(Exception):
    pass


class ParamHandler(metaclass=ABCMeta):
    types = {}


    def __init__(self, source):
        self.source = source
        #self.params = {}


    # def add_param(self, key, value):
    #     self.params[key] = value
    #
    #
    # def get_all_params(self):
    #     return self.params


    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass


    @classmethod
    def add_type(cls, name, klass):
        """кладем в словарь пару из названия типа и соответствующего обработчика """
        if not name:
            raise ParamHandlerException('Type must have a name!')
        if not issubclass(klass, ParamHandler):
            raise ParamHandlerException(
            'Class "{}" is not ParamHandler!'.format(klass)
            )
        cls.types[name] = klass


    @classmethod
    def get_instance(cls, source, *args, **kwargs):
        """вызываем необходимый обработчик, который оказался в имени класс"""
    # Шаблон "Factory Method"
        _, ext = os.path.splitext(str(source).lower())
        ext = ext.lstrip('.')
        klass = cls.types.get(ext)

        if klass is None:
            raise ParamHandlerException(
            'Type "{}" not found!'.format(ext)
            )

        return klass(source, *args, **kwargs)





class PickleParamHandler(ParamHandler):


    def read(self):
        """
        Чтение из текстового файла и присвоение значений в self.params
        """
        #print('returned!!!')
        with open(self.source, 'rb') as f:
            self.params = pickle.load(f)
            return self.params



    def write(self, data):

        with open(self.source, 'wb') as f:
            self.params = data
            pickle.dump(self.params, f)


class JsonParamHandler(ParamHandler):

    def read(self):
        pass


    def write(self):
        pass


def main():
    ParamHandler.add_type('pickle', PickleParamHandler)
    test_read = ParamHandler.get_instance('test.pickle')

    test_read.write('data')

if __name__ == main():
    main()
