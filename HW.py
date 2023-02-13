#1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

list = [1, 5, 8, 4, 6, 8, 1, 0]
print(list)
i = 0
sum = 0
while i < len(list):
    if i % 2 != 0:
        sum += list[i] 
    i+=1

print(sum)

#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

"""list = [2, 5, 8, 9, 3, 5, 4]

i = 0
k = len(list)-1
while i < len(list)//2:
    while k > len(list)//2:
        print(list[k]*list[i])
        i+=1
        k-=1"""

#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

"""list = [1.02, 1.2, 3.8, 5, 10.01]

i = 1
k = 1
max = round(list[0] % 1, 2)
min = round(list[0] % 1, 2)

while (i < len(list)):
    if list[i] % 1 > max:
        max = round(list[i] % 1, 3)
    if list[i] % 1 < min and list[i] % 1 != 0:
        min = round(list[i] % 1, 3)
    i += 1

print(list)
print(max, min)
print(max - min)"""

#Напишите программу, которая будет преобразовывать десятичное число в двоичное.

"""num = int(input("Введите целое двоичное число: "))
N =""
while (num != 0):
    N = str(num % 2) + N
    num //= 2

print(N)"""

#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

"""n = int(input('Введите число: '))

def get_fibonacci(n):
    fibo_nums = []
    a, b = 1, 1
    for i in range(n):
        fibo_nums.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (n+1):
        fibo_nums.insert(0, a)
        a, b = b, a - b
    return fibo_nums

fibo_nums = get_fibonacci(n)
print(get_fibonacci(n))
print(fibo_nums.index(0))"""



    


