immutable_var = (['Python', 24], 345, 2.9, False)

print(immutable_var)

# immutable_var[1] = 1
# Выдаст ошибку, поскольку кортежотносится к неизменяемому типу данных

mutable_list = [1, 4.2, False, 'Type']
mutable_list.insert(0, True)

print(mutable_list)
