"""
Функция для подсчета суммы четных числе в списке.
"""


def sum_numbers(list_numbers):
    """
    Функция принимает 1 аргумент - список чисел. Затем с помощью for
    проходит по каждому элементу списка, проверяет его на принадлежность к
    типу int и затем с помощью операции num % 2 вычисляет четные число.
    Функция возращает целое число - сумму четных чисел.
    Если аргумент не явялется списком, то падает исключение TypeError
    Если список пуст - то возвращается - 0
    Если список не имеет четных чисел, то возвращается - 0
    """
    if not isinstance(list_numbers, list):
        raise TypeError("Передаваемый объект не является списком.")

    sum_even_numbers = 0
    for num in list_numbers:
        try:
            if type(num) == int or (type(num) == str and num.isalnum()):
                num = int(num)
                if num % 2 == 0:
                    sum_even_numbers += num
        except ValueError:
            continue

    return sum_even_numbers


print(sum_numbers([True, False, 2, "100", "2.8"]))

#  Тест кейсы:
# sum_numbers('lsd') - TypeError: Передаваемый объект не является списком.
# sum_numbers([1, 1, 1, 1,]) - 0
# sum_numbers([2, 2, 2]) - 6
# sum_numbers([2, 1, -2, 5, 6]) - 6
# sum_numbers([]) -  0
# sum_numbers([2.5, 2.7, 1.1, 2.8, 2]) - 2
# sum_numbers([2, '4', 2]) - 4
# sum_numbers([None, 2]) - 2
# sum_numbers([True, False, 2]) - 2
# sum_numbers([True, False, 2, '100']) - 102
# sum_numbers([True, False, 2, '100', '2.8']) - 102
