def sort_task_date(list_tasks):
    return list_tasks['date']

def uncompleted_tasks(list_tasks):
    if not isinstance(list_tasks, list):
        raise TypeError("Передаваемый объект не является списком")
    if not list_tasks():
        raise ValueError("Список задач пустой")
    
    
    list_uncompleted_tasks = [task for task in list_tasks if i["status"] != "Выполнено" and isinstance(task, dict)]
    
    sorted_result = sorted(list_uncompleted_tasks, key=sort_task_date)

    return sorted_result



list_tasks = [
    {
        'name': 'Синергет', 'status': 'В работе', 'date': '12.05.2026'
    },
        {
        'name': 'Муром', 'status': 'Сделать', 'date': '11.05.2026'
    },
        {
        'name': 'Али', 'status': 'Выполнено', 'date': '14.05.2026'
    },
    
        ]


print(uncompleted_tasks(list_tasks))


'''
параметр key в sorted помогает сортировать значения по передаваемой функции.
labmda - это анонимная функция, которую можно написать в одну строчку
lambda x: x*2 будет эквивалентна
def test_lambda(x):
    return x*2
    

'''
