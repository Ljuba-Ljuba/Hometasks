"""
Требуется реализовать декоратор с параметрами return_namedtuple, который в случае, если функция возвращает кортеж, подменяет его именованным кортежем. Имена задаются в параметрах декоратора.

Для проверки типа данных переменной использовать функцию isinstance(переменная, тип).

Именованный кортеж находится в стандартном модуле collections.

(!) Декоратор универсальный, количество имен в кортеже переменное.

Имя файла
task_06_03.py
Имя функции-декоратора
return_namedtuple
Пример использования №1
@return_namedtuple('one', 'two')
def func():
    return 1, 2

Пример использования №2
@return_namedtuple('one', 'two', 'three')
def func():
    return 1, 2, 3

"""


from collections import namedtuple


def return_namedtuple(*names):
    def decorator(func):
        def wrapper(*args,**kwargs):
            first_tuple = func(*args,**kwargs)
            if isinstance(first_tuple, tuple):
                s = [*names]
                if len(s) != len(first_tuple):
                    raise ValueError('Invalid names')
                new_tuple = namedtuple('new_tuple',[*names])
                p = new_tuple(*first_tuple)
                #print(p.two)
                return p

            return first_tuple
        return wrapper
    return decorator
