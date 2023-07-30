#задача 1 необязательная. Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление.
#Функции bin и oct используйте для проверки своего результата.
#*Дополнительно
#Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
#Избегайте магических чисел
#Добавьте аннотацию типов где это возможно
#Используйте функции

digit = int(input('Введите число: '))

def binary(number):
    list_1 = []
    while number != 0:
        a = number % 2
        number = number // 2
        list_1.append(a)

    return list_1[::-1]

def octal(number):
    list_1 = []
    while number != 0:
        a = number % 8
        number = number // 8
        list_1.append(a)

    return list_1[::-1]

print(*binary(digit))
print(*octal(digit))