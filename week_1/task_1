def sum_numbers(list_numbers):
    if isinstance(list_numbers, list) and len(list_numbers) != 0:
        sum_positive_numbers = 0
        for i in list_numbers:
            if i % 2 == 0:
                sum_positive_numbers += i
    elif isinstance(list_numbers, list) and len(list_numbers) == 0:
        raise ValueError("Список пуст.")
    else:
        raise TypeError("Передаваемый объект не является списком.")

    return sum_positive_numbers


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
