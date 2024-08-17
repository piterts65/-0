first=input('Введите первое число: ')
second=input('Введите второе число: ')
third=input('введите третье число: ')
if first==second==third:
    print('одинаковых чисел:',3)
elif first==second or first==third or second==third:
    print('одинаковых чисел:',2)
elif first!=second!=third:
    print('одинаковых чисел:',0)


