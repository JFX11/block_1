def return_date(task):
    return task["date"]


def return_name(task):
    return task["name"]


def check_required_key(item):
    if not "name" in item:
        raise ValueError("В задаче отсутсвует обязательный ключ name")
    if not "status" in item:
        raise ValueError("В задаче отсутсвует обязательный ключ status")


def uncompleted_tasks(list_tasks):
    if not isinstance(list_tasks, list):
        raise TypeError("Передаваемый объект не является списком")
    if not list_tasks:
        raise ValueError("Список задач пустой")

    list_uncompleted_tasks = []
    list_not_date_tasks = []
    nums_dict = 0
    for item in list_tasks:
        if isinstance(item, dict):
            nums_dict += 1
            check_required_key(item)
            if item.get("status") != "Выполнено" and item.get("date"):
                list_uncompleted_tasks.append(item)
            elif item.get("status") != "Выполнено" and not item.get("date"):
                list_not_date_tasks.append(item)

    if not nums_dict:
        raise ValueError("Список не содержит задач")

    sorted_list_with_date = sorted(list_uncompleted_tasks, key=return_date)
    sorted_list_without_date = sorted(list_not_date_tasks, key=return_name)

    result_list = sorted_list_with_date + sorted_list_without_date

    return result_list


list_tasks = [
    {"name": "Синергет", "status": "В работе", "date": "2026-05-11"},
    {"name": "x", "status": "", "date": ""},
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

1. Сделал исключения, если в словаре не словарь или пустой словарь.
2. Мы будем считать, что у задачи 100% должен быть ключ 'name' и status
3. sorted сравнивает строки, которые отображаются в формате YYYY-MM-DD
Дполнительно сортируются задачи без этого параметра, а затем склеиваются, чтобы
получить финальный ответ

P.s если все задачи выолнены, возращается пустой список []


Тест кейсы:
list_tasks = [] - ValueError: Список задач пустой


list_tasks = 5   - TypeError: Передаваемый объект не является списком


list_tasks = [5]   - ValueError: Список не содержит задач


list_tasks = [
    {"name": "Синергет", "status": "В работе", "date": "2026-05-11"},
    {"name": "Муром", "status": "Сделать", "date": "2026-05-15"},
    [5],
] - [{'name': 'Синергет', 'status': 'В работе', 'date': '2026-05-11'}, {'name': 'Муром', 'status': 'Сделать', 'date': '2026-05-15'}]


list_tasks = [{}] - ValueError: В задаче отсутсвует обязательный ключ name


list_tasks = [{1}] - ValueError: Список не содержит задач


list_tasks = [
    {"name": "Синергет", "status": "В работе", "date": "2026-05-11"},
    {"name": "Муром", "status": "Сделать", "date": "2026-05-15"},
    {"name": "Али", "status": "Выполнено", "date": "2026-05-14"},
    {
        "name": "Али",
        "status": "В работе",
    },
] - [{'name': 'Синергет', 'status': 'В работе', 'date': '2026-05-11'}, {'name': 'Муром', 'status': 'Сделать', 'date': '2026-05-15'}, {'name': 'Али', 'status': 'В работе'}]

    
list_tasks = [
    {"name": "Синергет", "status": "Выполнено", "date": "2026-05-11"},
    {"name": "Муром", "status": "Выполнено", "date": "2026-05-15"},
    {"name": "Али", "status": "Выполнено", "date": "2026-05-14"},
    {
        "name": "Али",
        "status": "Выполнено",
    },
] - []


list_tasks = [
    {"name": "Синергет", "status": "В работе", "date": "2026-05-11"},
    {"name": "x", "status": "", "date": ""},
] - [{'name': 'Синергет', 'status': 'В работе', 'date': '2026-05-11'}, {'name': 'x', 'status': '', 'date': ''}]
"""
