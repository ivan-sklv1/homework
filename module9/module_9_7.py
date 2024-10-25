def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        for i in range(2, res - 1):
            if res % i == 0:
                print('Составное')
                return res
            else:
                print('Простое')
                return res
    return wrapper

@is_prime
def sum_three(a, b, c):
    total  = a + b + c
    return total

result = sum_three(2, 3, 6)
print(result)
