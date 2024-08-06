def calculate_structure_sum(*args):
    total_size = 0
    for element in args:
        if isinstance(element, list):
            total_size += calculate_structure_sum(*element)
        elif isinstance(element, dict):
            for key, value in element.items():
                if isinstance(value, str) and isinstance(key, int) or isinstance(key, float):
                    total_size += key + len(value)
                elif isinstance(value, int) or isinstance(value, float) and isinstance(key, str):
                    total_size += len(key) + value
                elif isinstance(value, str) and isinstance(key, str):
                    total_size += len(key) + len(value)
                elif isinstance(value, int) or isinstance(value, float) and isinstance(key, int) or isinstance(key, float):
                    total_size += key + value
        elif isinstance(element, tuple):
            total_size += calculate_structure_sum(*element)
        elif isinstance(element, set):
            total_size += calculate_structure_sum(*element)
        elif isinstance(element, str):
            total_size += len(element)
        elif isinstance(element, int) or isinstance(element, float):
            total_size += element
    return total_size


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
