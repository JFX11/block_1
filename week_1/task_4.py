def read_file(name_file):

    try:
        for line in open(name_file, "r", encoding="itf-8"):
            number_string = 0
            number_string += 1

        return number_string

    except FileNotFoundError:
        raise FileNotFoundError(f"Файл: '{name_file}' не найден")


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
