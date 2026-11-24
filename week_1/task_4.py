def read_file(name_file):

    try:
        with open(name_file, "r", encoding="utf-8") as file:
            if not file.read().strip():
                raise ValueError(f"Файл {name_file} пустой")
            
            file.seek(1)
            number_lines = 0
            for line in file:
                if line.strip():
                    number_lines += 1
            
            
        return number_lines

    except FileNotFoundError:
        raise FileNotFoundError("Файл не найден!")


def write_file(number_string):
    with open("res.txt", "w", encoding="utf-8") as file:
        file.write(str(number_string))


write_file(read_file("text.txt"))


"""
Программа откртывает файл и если в нем есть данные, то считает строки с помощью for.
Исключение - если файл пустой или сожержит только пробелы, если есть символ \n, то строка считается
Счетчик теперь стартует с 0, и отображает верное кол-во строк
прочитал, что file.read() ставит курсор в конец файла, поэтому после этого, использование
file.readlines будет одавать пустые данные. Для этого можно использовтаь file.seek(1)
это перемещает курсор в начало.(Почитать из форума, по использованию)

2. Тест кейсы:

write_file(read_file("teut.txt")) - FileNotFoundError: Файл не найден!

write_file(read_file("text.txt"))(пустой файл) - ValueError: Файл text.txt пустой

write_file(read_file("text.txt"))(файл только с пробелами) - ValueError: Файл text.txt пустой

write_file(read_file("text.txt"))(1 строка) - число в файле res = 1
write_file(read_file("text.txt"))(3 строки) - число в файле res = 3
write_file(read_file("text.txt"))(10 строк) - число в файле res = 10
"""
