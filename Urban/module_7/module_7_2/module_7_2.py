def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    line = 1
    strings_positions = {}

    for element in strings:
        strings_positions[(line, file.tell())] = element
        file.write(f'{element}\n')
        line += 1

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
