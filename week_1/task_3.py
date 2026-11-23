def sort_task_date(task):
    return task['date']

def uncompleted_tasks(list_tasks):
    if not isinstance(list_tasks, list):
        raise TypeError("Передаваемый объект не является списком")
    if not list_tasks:
        raise ValueError("Список задач пустой")
    
    
    list_uncompleted_tasks = [task for task in list_tasks if task["status"] != "Выполнено" and isinstance(task, dict)]
    
    sorted_result = sorted(list_uncompleted_tasks, key=sort_task_date)

    return sorted_result



list_tasks = [
    {
        'name': 'Синергет', 'status': 'В работе', 'date': '2026-05-11'
    },
        {
        'name': 'Муром', 'status': 'Сделать', 'date': '2026-05-15'
    },
        {
        'name': 'Али', 'status': 'Выполнено', 'date': '2026-05-14'
    },
    
        ]


print(uncompleted_tasks(list_tasks))


'''
параметр key в sorted помогает сортировать значения по передаваемой функции.
lambda - это анонимная функция, которую можно написать в одну строчку
lambda x: x*2 будет эквивалентна
def test_lambda(x):
    return x*2
Изменил формат времени на формат DDDD-MM-DD - теперь сортировка должна работать корректно
'''
