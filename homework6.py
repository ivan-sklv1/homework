# Dictionary
my_dict = {
    'Maria': 1998,
    'Stas': 2000,
    'Mihail': 1985
}

print(my_dict)
print(my_dict.get('Stas'))
print(my_dict.get('Ivan', 'Такого ключа нет'))

my_dict.update({
    'Ivan': 2001,
    'Max': 2005
})

print(my_dict.pop('Stas'))
print(my_dict)

# Set
my_set = {1, 2, 3, 3, 4, 'apple', 'apple', False}

print(my_set)

my_set.update({6, 9})

print(my_set)
