# Считываем три числа с клавиатуры
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))

# Проверяем каждое число и выводим те, которые попадают в интервал [1, 50]
if 1 <= num1 <= 50:
    print(num1)
if 1 <= num2 <= 50:
    print(num2)
if 1 <= num3 <= 50:
    print(num3)