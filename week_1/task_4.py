'''
Функция count_lines() принимает 1 аргумент, имя файла, затем открывает файл и считает с помощью цикла for кол-во строк файлов.
Элемент file считается итерируемым объектом, поэтому мы можем использовать это что-бы посчитать
кол-во строк в файле.
Функция write_count_lines принимает 2 аргумента, имя файла и результат функции count_lines(можно и просто целое число)
в данной задаче принимает именно результат функции.
'''

def count_lines(file_name):
    '''Функция подсчета строк из файла'''
    with open(file_name, "r", encoding="utf-8") as file:

        number_lines = 0
        for line in file:
            number_lines += 1
  
    return number_lines

#  Пустой файл - 0
#  Файла нет - FileNotFoundError
#  ' ' - 1
#  'x\n\n' - 2
#  \n\n\n - 3
#  10 строк 'как дела?' - 10
#  'x' - 1

      

def write_count_lines(file_name, count_lines):
    if type(count_lines) is not int:
        raise TypeError('Запись прервалась. Аргумент не является целым числом')
    if count_lines < 0:
        raise ValueError('Запись прервалась. Передаваемый аргумент должен быть неотрицательным числом')
    
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(str(count_lines))

write_count_lines('res.txt', count_lines('text.txt'))            


#  count_lines = 'тест' - TypeError('Запись прервалась. Аргумент не является целым числом')
#  count_lines = -5 - ValueError('Запись прервалась. Передаваемый аргумент должен быть неотрицательным числом')
#  count_lines = 5 - в файл записано число 5
#  count_lines = 3.5 - TypeError('Запись прервалась. Аргумент не является целым числом')
#  count_lines = True - TypeError('Запись прервалась. Аргумент не является целым числом')

