def read_file(name_file):

    try:
        with open(name_file, "r", encoding="utf-8") as file:

            if not file.read():
                raise ValueError(f"Файл {name_file} пустой")
            
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
Добавил проверку в функцию записи, на число

2. Тест кейсы:

a\nb\nc\n - в файл записано 3
привет\nмир\nкот\n - в файл записано 3
пустой файл - ValueError: Файл text.txt пустой
x - вернул 1
\n\n\n - вернул 3
"""
