import json
from pathlib import Path


def find_card(title, cards_list):
    """
    Ищет карточку по точному совпадению поля 'название' после нормализации
    (удаление пробелов по краям и приведение регистра).

    Получает:
        title (str): искомое название карточки.
        cards_list (list): список словарей карточек.

    Возвращает:
        dict | None: найденный словарь карточки или None, если совпадений нет.
    """
    normalized_title = title.strip().casefold()
    if normalized_title == "":
        return None

    for card in cards_list:
        if card["название"].strip().casefold() == normalized_title:
            return card
    return None


if __name__ == "__main__":
    cards_path = Path(__file__).resolve().parent.parent / "aleksandr" / "cards.json"
    with cards_path.open("r", encoding="utf-8") as file:
        cards = json.load(file)

    query = input("Введите название: ")

    if query.strip() == "":
        print("Введите название")
    else:
        found_card = find_card(query, cards)
        if found_card is not None:
            print("Ответ:", found_card["ответ"])
            print("Документ:", found_card["документ"])
            print("Страница:", found_card["страница"])
        else:
            print("Ответ не найден")
