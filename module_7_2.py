def custom_write(file_name, strings):
    strings_positions = {}
    li_numb = 1

    file = open(file_name, 'w', encoding='utf-8')
    for i in strings:
        b_pos = file.tell()
        file.write(f'{i}\n')
        strings_positions[(li_numb, b_pos)] = i
        li_numb += 1
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
