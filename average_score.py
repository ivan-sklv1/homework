grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
students.sort()

dictionary = dict(zip(students, grades))

dict_average = dict()
for name, score in dictionary.items():
    dict_average[name] = sum(score) / len(score)

print(dict_average)
