"""
Требуется реализовать декоратор с параметрами pause, который приостанавливает выполнение функции на указанное количество секунд.

В решении пригодится стандартный модуль time.

Имя файла
task_06_02.py
Имя функции-декоратора
pause
Пример использования
@pause(2)
def func():
    print('Фунция выполняется с задержкой!')
Задача №3
"""

import time

def pause(sec):
    def decorator(func):
        def wrapper(*args,**kwargs):
            #print('Функция выполняется с задержкой!')
            time.sleep(sec)
            return func(*args,**kwargs)
        return wrapper
    return decorator
