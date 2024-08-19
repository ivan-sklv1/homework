def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

test_function()
inner_function() # Выдает ошибку, поскольку данная функция находится в локальном пространстве имён функции test_function
# Вызовы работают наружу изнутри, но не внутрь
