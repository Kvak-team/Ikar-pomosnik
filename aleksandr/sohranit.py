import json
card = {
    'название': 'GRAPH',
    'ответ': 'Информация о задаче по графику',
    'документ': 'Prilizhenie po KEDM.pdf',
    'страница': 6
}

listjson = [card]

with open('cards.json', 'w', encoding="utf-8") as c:
    json.dump(listjson, c, ensure_ascii=False, indent=2)
