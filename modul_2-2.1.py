first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('введите третье число: '))
if first == second == third:
    print('одинаковых чисел:', 3)
elif first == second or first == third or second == third:
    print('одинаковых чисел:', 2)
else:
    print('одинаковых чисел:', 0)


