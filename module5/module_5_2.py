class House:
    def __init__(self, name, number_on_floors):
        self.name = name
        self.number_on_floors = number_on_floors

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_on_floors:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print('Такого этажа не существует.')
            
    def __len__(self):
        return self.number_on_floors
    
    def __str__(self) -> str:
        return f'Название: {self.name}, количество этажей: {self.number_on_floors}'


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

print(h1)
print(h2)

print(len(h1))
print(len(h2))
