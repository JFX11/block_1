def read_file(name_file):

    try:
        with open(name_file, "r", encoding="utf-8") as file:

            #if not file.read():
             #   raise ValueError(f"Файл {name_file} пустой")
            
            file.seek(0)
            number_lines = 0
            for line in file:
                print(line)
                number_lines += 1
            
            
        return number_lines

    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {name_file} не найден!")


def write_file(number_string):
    if isinstance(number_string, (int, float)):
        with open("res.txt", "w", encoding="utf-8") as file:
            file.write(str(number_string))
    


write_file(read_file("text.txt"))

"""
Эксперимет с seek поазал:
 1
 \nb\nc\n
 0
 a\nb\nc\n
Я понял, что seek(0) ставит указатель в начало а не 1

Строка это набор букв, слов. В нашем примере это еще знак `\n`, перевод на новую стрроку
Пустой файл. Это файл, который полностью пустой, в нем нет ничего

2. Тест кейсы:

write_file(read_file("teut.txt"))

write_file(read_file("text.txt"))(пустой файл)

write_file(read_file("text.txt"))(файл только с пробелами)

write_file(read_file("text.txt"))(1 строка)
write_file(read_file("text.txt"))(3 строки)
write_file(read_file("text.txt"))(10 строк)
"""
