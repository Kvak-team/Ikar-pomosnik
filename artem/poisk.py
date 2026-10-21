# Карточки справочной информации
file_card = {
    "название": "FILE",
    "ответ": "отвечает за управление файлами, удаление или добавление графика",
    "документ": "Prilizhenie po KEDM.pdf",
    "страница": 6,
}

graph_card = {
    "название": "GRAPH",
    "ответ": "Информация о задаче по графику",
    "документ": "Prilizhenie po KEDM.pdf",
    "страница": 6,
}

diagnosis_card = {
    "название": "DIAGNOSIS",
    "ответ": "отображение аварийных сообщений",
    "документ": "Prilizhenie po KEDM.pdf",
    "страница": 6,
}


# Список всех доступных карточек
cards = [file_card, graph_card, diagnosis_card]


def find_card(title, cards_list):
    """
    Ищет карточку в списке по точному совпадению поля 'название'.
    Возвращает найденный словарь карточки или None, если совпадений нет.
    """
    for card in cards_list:
        if card["название"] == title:
            return card
    return None


# Ввод названия с клавиатуры
query = input("Введите название: ")

# Проверка ввода и вывод результата
if query == "":
    print("Введите название")
else:
    found_card = find_card(query, cards)
    if found_card is not None:
        print("Ответ:", found_card["ответ"])
        print("Документ:", found_card["документ"])
        print("Страница:", found_card["страница"])
    else:
        print("Ответ не найден")
