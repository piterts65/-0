my_dict={'Коля': 178,'Вася': 192, 'Оля': 157, 'Рома': 180}
print(my_dict)
print(my_dict['Оля'])
print(my_dict.get('Зая','Рост неизвестен'))
my_dict.update({'Валера': 173, 'Сева': 175})
a=my_dict.pop('Рома')
print(a)
print(my_dict)

my_set={1,'лось',14,15,0.5,1,2,3.14,(1,2,3),}
print('Set:',my_set)
my_set.add(6)
my_set.discard(3.14)
my_set.remove((1,2,3))
Modified_set=my_set
print('Modified set:',Modified_set)