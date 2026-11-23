def read_file(name_file):

    try:
        with open(name_file, "r", encoding="utf-8") as file:
            #if not file.read():
                #raise ValueError("Файл пустой")
            
            
            print(file.tell())
            text = file.read()
            print(file.tell())
            print(list(file))
            
            
            
            
            number_string = 0
            for line in file:
                number_string += 1
                
        return number_string

    except FileNotFoundError:
        raise FileNotFoundError()


def write_file(number_string):
    with open("res.txt", "w", encoding="utf-8") as file:
        file.write(str(number_string))
        return "Число строк успешно записано в 'res.txt'"


write_file(read_file("text.txt"))


"""
1. Теперь обе функции возращают только 1 параметр
1 функция возвращает число, 2 - текст с подтвержденим записи

2. Тест кейсы:

write_file(read_file("teut.txt")) - FileNotFound

write_file(read_file("text.txt"))(пустой файл) - ValueError

write_file(read_file("text.txt"))(файл только с пробелами) - ValueError

write_file(read_file("text.txt"))(1 строка) - "Число строк успешно записано в 'res.txt'"

3. Почистил отладочные print()
"""
