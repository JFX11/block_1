def sum_numbers(list_numbers):
    sum_even_numbers = 0
    if not isinstance(list_numbers, list):
        raise TypeError("Передаваемый объект не является списком.")
    elif len(list_numbers) == 0:
        raise ValueError("Список пуст.")
    else:
        for num in list_numbers:
            if isinstance(num, (int, float)) and num % 2 == 0:
                sum_even_numbers += int(num)
        
    return sum_even_numbers

print(sum_numbers([2.5, 2.7, 1.1, 2.8, 2]) )

"""
Новые правки:
Изменил наименование на sum_even_numbers(сумма четных чисел) и поменял i - на num
Теперь коде проверяется каждый элмент списка, если не число, то пропускается
Добавил, чтобы результат, всегда был числом типа int
Применил в функции guard clauses - сначала обрабатываются отрицательные сценарии, а в конце положительные
Упростил выражение if len(...) != 0, на просто elif len(list_numbers) == 0: raise ...

Тест кейсы:
sum_numbers('lsd') - TypeError: Передаваемый объект не является списком.
sum_numbers([1, 1, 1, 1,]) - 0 
sum_numbers([2, 2, 2]) - 6 
sum_numbers([2, 1, -2, 5, 6]) - 6 
sum_numbers([]) -  ValueError: Список пуст.
sum_numbers([2.5, 2.7, 1.1, 2.8, 2]) - 2
"""
