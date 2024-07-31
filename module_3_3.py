def print_params(a=1, b='строка', c=True):
    print(a, b, c)


values_list = [1, True, 'pool']
values_dict = {'a': 2, 'b': False, 'c': 'moon'}
values_list_2 = [88, 'hope']

print_params()
print_params(b=25, c=[1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
