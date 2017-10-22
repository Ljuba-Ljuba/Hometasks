"""
Реализовать генератор случайных паролей указанной длины.

В пароле можно использовать любые символы в верхнем и нижнем регистре.

Например: password_generator(16), вернет случайный пароль длиной 16 символов.

Пригодится стандартный модуль random

Имя файла
task_07_02.py
Имя функции-генератора
password_generator
Возвращаемое значение
Генератор

"""
import random
from string import digits, ascii_letters


def password_generator(n):
    listing = list(digits + ascii_letters)
    for i in range(n):
        letter = random.choice(listing)
        yield letter
