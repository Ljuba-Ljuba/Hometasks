'''
Задача №1.
Файл "data.txt" заполнен случайными целыми числами, числа разделены одним пробелом.
1. Сформировать файл "out-1.txt" из элементов файла "data.txt", делящихся без остатка на n
2. Сформировать файл "out-2.txt" из элементов файла "data.txt", возведенных в степень p
n и p - целые числа, вводимые с клавиатуры.
Имя файла: task_04_01.py
Тестовый набор данных №1:
Содержимое файла data.txt: 48 48 3 75 26 57 53 21 71 15
Входные данные: 2 3
Содержимое файла out-1.txt: 48 48 26
Содержимое файла out-2.txt: 110592 110592 27 421875 17576 185193 148877 9261 357911 3375
'''

with open('data.txt') as f:
    loaded_data = f.read()
    loaded_data = loaded_data.split(' ')


n = int(input())
p = int(input())
x1 = []
x2 = []
for num in range(len(loaded_data)):
    loaded_data[num]=int(loaded_data[num])
    x2.append(str(loaded_data[num]**p))

    if (loaded_data[num]) // n == (loaded_data[num]) / n:
        x1.append(str(loaded_data[num]))


with open('out-1.txt','a') as new1:
    new1.write(" ".join(x1))
with open('out-2.txt','a') as new2:
    new2.write(" ".join(x2))
