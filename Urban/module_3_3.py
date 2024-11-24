values_list = ['Элемент', 1, True]
values_list_2 = [2.25, 'string']
values_dict = {'a': 'Maksim', 'b': 32, 'c': True}


def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(a=4, b=2, c=3)
print_params(b=25)
print_params(c=[1, 2, 3])
print()
print_params(*values_list)
print_params(**values_dict)
print()
print_params(*values_list_2, 42)
