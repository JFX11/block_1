def sum_numbers(list_numbers):
    if not isinstance(list_numbers, list):
        raise TypeError("Передаваемый объект не является списком.")
    if not list_numbers:
        raise ValueError("Список пуст.")
    
    sum_even_numbers = 0
    for num in list_numbers:
        if isinstance(num, (int, float)) and num % 2 == 0:
            sum_even_numbers += int(num)
        
    return sum_even_numbers

print(sum_numbers([True, False, 2]))
print(int(True))

"""
Новые правки:
1. Убрал блок else, т.к если происходит исключение, происходит выход из функции, переменную
sum_even_numbers перенес после блока с исключениями
2. Добавил два кейса sum_numbers([2, '4', 2]) и sum_numbers([None, 2])
3. Поправил elif на if not list_numbers
sum_numbers([True, False, 2]) - данный кейс содержат True и False - они отбрасываются с помощью isinstance, т.к
эта функция смотрит и на подклассы, если бы использовали type(), то True и False прошли бы, т.к эквивалентны 1 и 0

Тест кейсы:
sum_numbers('lsd') - TypeError: Передаваемый объект не является списком.
sum_numbers([1, 1, 1, 1,]) - 0 
sum_numbers([2, 2, 2]) - 6 
sum_numbers([2, 1, -2, 5, 6]) - 6 
sum_numbers([]) -  ValueError: Список пуст.
sum_numbers([2.5, 2.7, 1.1, 2.8, 2]) - 2
sum_numbers([2, '4', 2])
sum_numbers([None, 2])
sum_numbers([True, False, 2]) - 2
"""
