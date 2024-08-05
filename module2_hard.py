import random

n = random.randint(3, 21)
result = []

for i in range(1, n):
    for j in range(i, n):
        if i == j:
            continue
        if n % (i + j) == 0:
            result.append(str(i) + str(j))
print(n, '-', *result, sep='')
