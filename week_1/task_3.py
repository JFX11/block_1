def sort_task(n):
    result = [i for i in n if i["status"] != "Выполнено"]

    sorted_result = sorted(result, key=lambda x: x["date"])

    return sorted_result
