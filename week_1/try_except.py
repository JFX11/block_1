from datetime import datetime

list_tasks = [
    {"name": "Синергет", "status": "В работе", "date": "2026-05-11"},
    {"name": "Муром", "status": "Сделать", "date": "15.05.2026"},
]

valid_date = str(datetime.strptime(list_tasks[1]["date"], "%d.%m.%Y"))
print(valid_date)
