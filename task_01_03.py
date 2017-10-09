#3-я задача 1ой домашки
#Задача рассортировать 3 целых числа и вывести их через запятую

#вводим по одному три целых числа
a=int(input())
b=int(input())
c=int(input())

#переменные, в которые будем ставить значения по возрастанию
list1=0 # самое маленькое число
list2=0 # второе число итогового списка
list3=0 # самое большое списка

if a<=b:
    list1=a if a<=c else c
    list3=b if b>c else c

    if a<=c:# при list1=a
        list2=b if b<=c else c
    if a>c: # при list1=c
        list2=a
elif a>b: # проверяем при a>b
    list1=b if b<=c else c
    list3=a if a>c else c
    if b<=c: # при list1=b
        list2=a if a<=c else c
    if b>c:# при list1=c
        list2=b

print(list1,list2,list3, sep=", ")
