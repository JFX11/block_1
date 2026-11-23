def dict_item(task):
    return task["date"]


def examination_dict(item):
    if not item.get("status"):
        print(
            f"У задачи {item['name']} отсутсвует статус. Вставлено значение по умолчанию\n"
        )
        item["status"] = item.get("status", "Неизвестно")

    if not item.get("date"):
        print(
            f"У задачи {item['name']} отсутсвует дата. Вставлено значение по умолчанию\n"
        )
        item["date"] = item.get("date", "Неизвестно")


def uncompleted_tasks(list_tasks):
    if not isinstance(list_tasks, list):
        raise TypeError("Передаваемый объект не является списком")
    if not list_tasks:
        raise ValueError("Список задач пустой")

    list_uncompleted_tasks = []
    nums_dict = 0
    for item in list_tasks:
        if isinstance(item, dict):
            nums_dict += 1
            examination_dict(item)
            if item.get("status") != "Выполнено":
                list_uncompleted_tasks.append(item)

    if not nums_dict:
        raise ValueError("Список не содержит задач")

    sorted_result = sorted(list_uncompleted_tasks, key=dict_item)

    return sorted_result


list_tasks = [
    {"name": "Синергет", "status": "Выполнено", "date": "2026-05-11"},
    {"name": "Муром", "status": "Выполнено", "date": "2026-05-15"},
    {"name": "Али", "status": "Выполнено", "date": "2026-05-14"},
    {
        "name": "Али",
        "status": "Выполнено",
    },
]


print(uncompleted_tasks(list_tasks))


"""
параметр key в sorted помогает сортировать значения по передаваемой функции.
lambda - это анонимная функция, которую можно написать в одну строчку
lambda x: x*2 будет эквивалентна
def test_lambda(x):
    return x*2
Изменил формат времени на формат YYYY-MM-DD - теперь сортировка должна работать корректно


Я не до конца смог разобраться как именно нам сортировать даты, если он нам поступают в
разных форматак. Поэтому мы будем требовать по ТЗ, чтобы формат даты был YYYY-MM-DD

1. Сделал исключения, если в словере не словарь или пустой словарь.
2. Мы будем считать, что у задачи 100% должен быть ключ 'name'
3. sorted сравнивает строки, которые отображаются в формате YYYY-MM-DD

P.s если все задачи выолнены, возращается пустой список []
Так-же добавил print, если в задачи отсутсвует ключ, чтобы информировать пользователя
что у вставилось значение по умолчанию

Тест кейсы:
list_tasks = [] - ValueError: Список задач пустой
list_tasks = 5   - TypeError: Передаваемый объект не является списком
list_tasks = [5]   - ValueError: Список не содержит задач
list_tasks = [
            {"name": "Синергет", "status": "В работе", "date": "2026-05-11"},
            {"name": "Муром", "status": "Сделать", "date": "2026-05-15"},
            [5],
            ]   - [{'name': 'Синергет', 'status': 'В работе', 'date': '2026-05-11'}, 
                    {'name': 'Муром', 'status': 'Сделать', 'date': '2026-05-15'}]
list_tasks = [{}] - ValueError: Задача пустая
list_tasks = [{1}] - ValueError: Список не содержит задач
list_tasks = [
    {"name": "Синергет", "status": "В работе", "date": "2026-05-11"},
    {"name": "Муром", "status": "Сделать", "date": "2026-05-15"},
    {"name": "Али", "status": "Выполнено", "date": "2026-05-14"},
    {
        "name": "Али",
        "status": "В работе",
    },
] - [{'name': 'Синергет', 'status': 'В работе', 'date': '2026-05-11'}, 
    {'name': 'Муром', 'status': 'Сделать', 'date': '2026-05-15'}, {'name': 'Али', 'status': 'В работе', 'date': 'Даты нет'}, 
    {'name': 'Али', 'status': 'Статуса нет', 'date': 'Даты нет'}]

list_tasks = [
    {"name": "Синергет", "status": "Выполнено", "date": "2026-05-11"},
    {"name": "Муром", "status": "Выполнено", "date": "2026-05-15"},
    {"name": "Али", "status": "Выполнено", "date": "2026-05-14"},
    {
        "name": "Али",
        "status": "Выполнено",
    },
] - []
"""
