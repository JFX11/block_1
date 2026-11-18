def sum_numbers(list_numbers):
    sum_even_numbers = 0
    if len(list_numbers) != 0:
        if isinstance(list_numbers, list):
            for num in list_numbers:
                if isinstance(num, (int, float)) and num % 2 == 0:
                    sum_even_numbers += int(num)
        elif isinstance(list_numbers, list) and len(list_numbers) == 0:
            raise ValueError("Список пуст.")
        else:
            raise TypeError("Передаваемый объект не является списком.")

    return sum_even_numbers

print(sum_numbers([2, 2.0, 1, 'дав']))

"""
Изменил имена переменных на понятные. Убрал использование генераторов списков 
и функции sum. Заменил на for. Изменил функцию type() на isinstance() т.к
в документации говоритьс, что она учитывает и подклассы и лучше подходит для
такого сравнения.
Добавил исключения, теперь функция всегда возращает только число, а если нет, то
происходит ошибка с выводом информации.
По ТЗ нам нужно было обрабатывать именно список. Поэтому сделал так, что если мы 
передаем что-либо кроме списка, то появляется исключение.
"""
