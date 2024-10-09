def custom_write(file_name:str, strings:list):
    strings_positions = {}
    file = open(file_name, 'w', encoding='utf8')
    nums = enumerate(strings, start=1)
    for string in strings:
        for index, string in nums:
            position = file.tell()
            file.write(string + '\n')
            strings_positions[index, position] = string
        file.close()
        return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
