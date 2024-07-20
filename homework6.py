my_dict = {'Sem': 1997, 'Ron': 1990, 'Tedd': 2001, 'Bill': 1993}
print(my_dict)
print(my_dict['Ron'])
print(my_dict.get('Mike'))
my_dict.update({'Van': 1999, 'Ned': 2005})
dlt = my_dict.pop('Bill')
print(dlt)
print(my_dict)

my_set = {1, 2, 3, 1, 8, 12, 8, 4, 'Sad', 3}
print(my_set)
print(my_set.add(5))
print(my_set.add(10))
print(my_set.discard(3))
print(my_set)

