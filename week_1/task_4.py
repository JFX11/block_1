def lines_number(file_name):
    with open(file_name, "r", encoding="utf-8") as file:

        count_lines = 0
        for line in file:
            count_lines += 1
  
    return count_lines
      

def write_count_lines(file_name, count_lines):
    if type(count_lines) is not int:
        raise TypeError('Запись прервалась. Аргумент не является целым числом')
    if count_lines < 0:
        raise ValueError('Запись прервалась. Передаваемый аргумент должен быть положительным числом')
    
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(str(count_lines))
            
write_count_lines('res.txt', lines_number('text.txt'))

"""
Строка это набор букв, слов. В нашем примере это еще знак `\n`, перевод на новую строку
Пустой файл. Это файл, который полностью пустой, в нем нет ничего - возвращает 0
Если файла на чтения нет - то ошибка FileNotFoundError

2. Тест кейсы:

write_file(read_file('text.txt'))(файл пустой) - ValueError: Файл text.txt пустой
write_file(read_file('text.txt'))(a\n\nb\n) - в файл записано 3
write_file(read_file('text.txt'))(пробел) - в файл записано 1
write_file(read_file('text.txt'))(привет без \n) - в файл записано 1
write_file(read_file('text.txt'))(10 строк) - в файл записано 10 строк
write_file(read_file('text.txt'))(\n\n\n) - в файл записано 3
write_file(read_file('texа.txt')) - FileNotFoundError: [Errno 2] No such file or directory: 'texа.txt'
write_file(read_file('text.txt'))('х') - в файл записано 1
write_file(read_file('text.txt'))(a\nb\nc") - в файл записано 3

"""
