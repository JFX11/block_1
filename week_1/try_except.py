from datetime import datetime

def validate_date(dict_item):
    try:
        valid_date = str(datetime.strptime(dict_item['date'], "%d.%m.%Y"))
        return valid_date[0:10]
    except ValueError:
        try:
            valid_date_1 = str(datetime.strptime(dict_item['date'], "%Y.%m.%d"))
            return valid_date_1[0:10]
        except ValueError:
            try:
                valid_date_2 = str(datetime.strptime(dict_item['date'], "%Y-%m-%d"))
                return valid_date_2[0:10]
            except ValueError:
                try:
                    valid_date_3 = str(datetime.strptime(dict_item['date'], "%d-%m-%Y"))
                    return valid_date_3[0:10]
                except ValueError:
                       try:
                           valid_date_4 = str(datetime.strptime(dict_item['date'], "%d:%m:%Y"))
                           return valid_date_4[0:10]
                       except ValueError:
                           try:
                                valid_date_5 = str(datetime.strptime(dict_item['date'], "%d:%m:%Y"))
                                return valid_date_5[0:10]
                           except ValueError:
                               return 0
                               
                   
                   
list_tasks = [
    {"name": "Синергет", "status": "В работе", "date": "2026-05-11"},
    {"name": "Муром", "status": "Сделать", "date": "15-05-2026"},
    {"name": "Муром", "status": "Сделать", "date": "15.05.2026"},
    {"name": "Синергет", "status": "В работе", "date": "2026.05.11"},
    {"name": "Синергет", "status": "В работе", "date": "мусор"},
]

for item in list_tasks:
    print(validate_date(item))

t = '2026.05.11'
correct_date = t.replace('.', '').replace('-', '').replace(':', '')
print(correct_date)