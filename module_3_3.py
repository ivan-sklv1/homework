def print_prams(a = 1, b = 'string', c = True):
    print(a, b, c)

print_prams(b = 25)
print_prams(c = [1,2,3])


values_list = (False, 3.5, 'Hello')
values_dict = {'a': '1.2', 'b': 5, 'c': 3.2}

print_prams(*values_list)
print_prams(**values_dict)


values_list_2 = [54.42, 'Python']
print_prams(*values_list_2, 25)
