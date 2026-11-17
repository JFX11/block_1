def read_file(name_file):

    number_string = 0
    try:
        with open(name_file, "r", encoding="utf-8") as file:
            print()
            for string in file:
                number_string += 1

        return number_string

    except FileNotFoundError:
        return f"Файл: {name_file} не найден"


def write_file(number_string):
    if number_string != 0:
        with open("res.txt", "w", encoding="utf-8") as file:
            file.write(str(number_string))
            print("Число успешно записано в 'res.txt'")
    else:
        print("Файл пустой")


write_file(read_file("файла_нет.txt"))


"""
1. В rex.txt появится имя файла файла_нет.txt. Винновата функция read.
Которая вернула строку и функция write, которая записала это
2. Т.к нам нужно записать именно число. Необходимо указать проверку
что мы получили число, а не строку с символами
3. Функция, которая общается с человеком
"""
