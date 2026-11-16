import json

with open('cards.json', 'r', encoding="utf-8") as c:
    listjson = json.load(c)

dictionary = {number["название"]: number for number in listjson}

for number in dictionary.values():
    if number.get('документ', 'error') == 'error' or number.get('документ') == "":
        print(f"название: {number.get('название')}\nУ карточки не указан источник.")
    else:
        print(f"название: {number.get('название')}\nответ: {number.get('ответ')}\nдокумент: {number.get('документ')}\nстраница: {number.get('страница')}")
