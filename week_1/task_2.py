def filter_str(word):
    new_word = ""
    for letter in word:
        if "а" <= letter <= "я":
            new_word += letter
        else:
            continue

    return new_word


def count_word(string):
    dict_words = {}
    print(string.lower().split())
    for i, word in enumerate(string.lower().split()):
        if filter_str(word) in dict_words:
            dict_words[filter_str(word)] += 1
        else:
            dict_words[filter_str(word)] = 1

    return dict_words


print(count_word("   привет           мир   "))


"ТЗ: Функция принимает строку текста и возвращает словарь: слово → сколько раз встретилось."
'''
Метод строк str.isalpha - проверяет, что строка состоит только из букв
Функция isinstance() - проверяет, что объект принадлежит к конктерному классу(учитываются и подкласса), поэтому лучше использовать эту
функцию, чем type()
dict.get - это метод словаря, которая позволяет обратиться к элементу словаря, через ключ. Данный метод отличается тем, что не вызывает
исключения, если элемента нет в словаре. По умолчанию указывается None, но можно указать 2 аргумент, что мы хотим получить
dict.get(обязательный аргумент(ключ), опциональный аргумент(Что хотим видеть, если значения не оказалось))

'''
'''
Слово - это объект, который содержит в себе только буквы.
'''

