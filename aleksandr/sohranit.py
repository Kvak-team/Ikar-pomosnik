import json
cardOne = {
    'название': 'GRAPH',
    'ответ': 'Информация о задаче по графику',
    'документ': 'Prilizhenie po KEDM.pdf',
    'страница': 6
}

cardTwo = {
    'название': 'FILE',
    'ответ': 'управление файлами, удаление или добавление графика',
    'документ': 'Prilizhenie po KEDM.pdf',
    'страница': 6
}

cardThree = {
    'название': 'DIAGNOSIS',
    'ответ': 'отображение аварийных сообщений',
    'документ': 'Prilizhenie po KEDM.pdf',
    'страница': 6
}
listjson = [cardOne, cardTwo, cardThree]

with open('cards.json', 'w', encoding="utf-8") as c:
    json.dump(listjson, c, ensure_ascii=False, indent=2)
