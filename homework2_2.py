first = input('Enter first number: ')
second = input('Enter second number: ')
third = input('Enter third number: ')

if first == second and second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
elif not first == second and not second == third:
    print(0)
