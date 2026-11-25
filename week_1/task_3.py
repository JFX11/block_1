from datetime import datetime


def check_required_key(item):
    if "name" not in item:
        raise ValueError("В задаче отсутствует обязательный ключ name")
    if "status" not in item:
        raise ValueError("В задаче отсутствует обязательный ключ status")


def check_from_dict(list_tasks):
    if not isinstance(list_tasks, list):
        raise TypeError("Передаваемый объект не является списком")
    if not list_tasks:
        raise ValueError("Список задач пустой")


def validate_date(object):
    try:
        valid_date = str(datetime.strptime(object["date"], "%d.%m.%Y"))
        return valid_date[0:10]
    except ValueError:
        try:
            valid_date_1 = str(datetime.strptime(object["date"], "%Y.%m.%d"))
            return valid_date_1[0:10]
        except ValueError:
            try:
                valid_date_2 = str(datetime.strptime(object["date"], "%Y-%m-%d"))
                return valid_date_2[0:10]
            except ValueError:
                try:
                    valid_date_3 = str(datetime.strptime(object["date"], "%d-%m-%Y"))
                    return valid_date_3[0:10]
                except ValueError:
                    try:
                        valid_date_4 = str(
                            datetime.strptime(object["date"], "%d:%m:%Y")
                        )
                        return valid_date_4[0:10]
                    except ValueError:
                        try:
                            valid_date_5 = str(
                                datetime.strptime(object["date"], "%d:%m:%Y")
                            )
                            return valid_date_5[0:10]
                        except ValueError:
                            return 0


def check_date(item):
    if "date" not in item:
        return False

    correct_date = item.get("date").replace(".", "").replace("-", "").replace(":", "")

    if correct_date.isdigit():
        return True
    return False


def uncompleted_tasks(list_tasks):

    check_from_dict(list_tasks)

    list_uncompleted_tasks = []
    list_not_date_tasks = []
    list_not_date_not_status = []
    nums_dict = 0

    for item in list_tasks:
        if isinstance(item, dict):
            nums_dict += 1
            check_required_key(item)
            if item.get("status") != "Выполнено" and check_date(item):
                list_uncompleted_tasks.append(item)
            elif item.get("status") == "":
                list_not_date_not_status.append(item)
            else:
                list_not_date_tasks.append(item)

    if not nums_dict:
        raise ValueError("Список не содержит задач")

    sorted_list_with_date = sorted(list_uncompleted_tasks, key=validate_date)
    sorted_list_without_date = sorted(
        list_not_date_tasks, key=lambda status: status["status"]
    )
    sorted_list_name = sorted(list_not_date_not_status, key=lambda name: name["name"])

    result_list = sorted_list_with_date + sorted_list_without_date + sorted_list_name

    return result_list


list_tasks = [
    {"name": "Синергет", "status": "В работе", "date": "2026-05-11"},
    {"name": "Али", "status": "В работе", "date": "12.05.2026"},
]

print(uncompleted_tasks(list_tasks))


"""
параметр key в sorted помогает сортировать значения по передаваемой функции.
lambda - это анонимная функция, которую можно написать в одну строчку
lambda x: x*2 будет эквивалентна
def test_lambda(x):
    return x*2
Изменил формат времени на формат YYYY-MM-DD - теперь сортировка должна работать корректно


Узнал что есть библитоека datetime и применил её для проверки правильности формата времени,
теперь если мы написали dd-mm-yyyy или dd.mm.yyyy, мы с помощью функции делаем корректный формат и сортируем по
этому параметру

1. Сделал исключения, если в словаре не словарь или пустой словарь.
2. Мы будем считать, что у задачи 100% должен быть ключ 'name' и status
3. sorted сравнивает строки, которые отображаются в формате YYYY-MM-DD
Дполнительно сортируются задачи без этого параметра, а затем склеиваются, чтобы
получить финальный ответ

P.s если все задачи выолнены, возращается пустой список []
Если передаваемая задча содержит status и date с пустыми занчениями,
то задача считается не выполненной и сортируется по имени после задач, которые с датой.

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
