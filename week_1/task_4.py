'''
Функция read_lines() - открывает файл и считает с помощью цикла for кол-во строк файлов.
Элемент file считается этерируемым объектом, поэтому мы можем использовать это что-бы посчитать
кол-во строк в файле.
'''

def count_lines(file_name):
    '''Функция подсчета строк из файла'''
    with open(file_name, "r", encoding="utf-8") as file:

        count_lines = 0
        for line in file:
            count_lines += 1
  
    return count_lines

'''
Тест-кейсы

Пустой файл - 0
Файла нет - FileNotFoundError
' ' - 1
'x\n\n' - 2
\n\n\n - 3
10 строк 'как дела?' - 10
'''
      

def write_count_lines(file_name, count_lines):
    if type(count_lines) is not int:
        raise TypeError('Запись прервалась. Аргумент не является целым числом')
    if count_lines < 0:
        raise ValueError('Запись прервалась. Передаваемый аргумент должен быть неотрицательным числом')
    
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(str(count_lines))
            

'''
Тест кейсы:
'тест' - TypeError('Запись прервалась. Аргумент не является целым числом')
-5 - ValueError('Запись прервалась. Передаваемый аргумент должен быть неотрицательным числом')
5 - в файл записано число 5
'''

