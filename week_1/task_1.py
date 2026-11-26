def sum_numbers(list_numbers):
    if not isinstance(list_numbers, list):
        raise TypeError("Передаваемый объект не является списком.")
    if not list_numbers:
        raise ValueError("Список пуст.")
    
    sum_even_numbers = 0
    for num in list_numbers:
        try:
            if type(num) == int or (type(num) == str and num.isalnum()):
                num = int(num)
                if num % 2 == 0:
                    sum_even_numbers += num
        except ValueError:
            continue
    
    if not sum_even_numbers:
        raise ValueError('В списке отсутствуют четные числа')
        
    return sum_even_numbers



"""
Новые правки:
1. Убрал блок else, т.к если происходит исключение, происходит выход из функции, переменную
sum_even_numbers перенес после блока с исключениями
2. Добавил два кейса sum_numbers([2, '4', 2]) и sum_numbers([None, 2])
3. Поправил elif на if not list_numbers
Изменил в функции проверку значеня, с isinstance на type(), чтобы не обрабатывать
булевые значения. isinstance - проверяет и подклассы. Поэтому раньше у меня bool проходил,
т.к он наследуется от int.


Тест кейсы:
sum_numbers('lsd') - TypeError: Передаваемый объект не является списком.
sum_numbers([1, 1, 1, 1,]) - ValueError: В списке отсутствуют четные числа 
sum_numbers([2, 2, 2]) - 6 
sum_numbers([2, 1, -2, 5, 6]) - 6 
sum_numbers([]) -  ValueError: Список пуст.
sum_numbers([2.5, 2.7, 1.1, 2.8, 2]) - 2
sum_numbers([2, '4', 2]) - 4
sum_numbers([None, 2]) - 2
sum_numbers([True, False, 2]) - 2
sum_numbers([True, False, 2, '100'] - 2

Заметил что не объеденил проверку типов int и float. Поэтому проходили нечетные числа
Прогнал все кейсы, результат корректный
"""
