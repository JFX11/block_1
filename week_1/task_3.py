def sort_task_date(list_tasks):
    return list_tasks['date']

def uncompleted_tasks(list_tasks):
    list_uncompleted_tasks = [i for i in list_tasks if i["status"] != "Выполнено"]
    
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