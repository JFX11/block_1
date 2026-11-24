def read_file(name_file):

        with open(name_file, "r", encoding="utf-8") as file:

            if not file.read():
                raise ValueError(f"Файл {name_file} пустой")
            
            file.seek(0)
            number_lines = 0
            for line in file:
                number_lines += 1
            
            
        return number_lines
      


def write_file(number_string):
    if not type(number_string) == int:
        raise TypeError('Запись прервалась. т.к аргумент не является числом')
    
    with open("res.txt", "w", encoding="utf-8") as file:
        file.write(str(number_string))
            
    


write_file(read_file('text.txt'))

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
Убрал перехват отсутсвия файла, заменил ValueError, если мы передаем не наименование файла

2. Тест кейсы:

write_file(read_file(1)) - ValueError: Передаваемый аргемент не является наименованием файла
write_file(read_file(text.txt))(файл пустой) - ValueError: Файл text.txt пустой
write_file(read_file(text.txt))(a\n\nb\n) - в файл записано 3
write_file(read_file(text.txt))(пробел) - в файл записано 1
write_file(read_file(text.txt))(привет без \n) - в файл записано 1
write_file(read_file(text.txt))(10 строк) - в файл записано 10 строк
"""
