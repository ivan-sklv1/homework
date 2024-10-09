from pprint import pprint


class Product:

    def __init__(
        self,
        name:str,
        weight:float,
        category:str
    ):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:

    def __init__(self, __file_name = 'products.txt'):
        self.__file_name = __file_name

    def get_products(self):
        file = open(self.__file_name, 'r')
        result = pprint(file.read())
        file.close()
        return result

    def add(self, *products):
        with open(self.__file_name, 'r') as file:
            data = file.read()
            for product in products:
                if product.name in data:
                    print('Товар уже есть в списке')
                else:
                    with open(self.__file_name, 'a') as file2:
                        file2.write(f"{product} \n")
                        file2.close()
            file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
