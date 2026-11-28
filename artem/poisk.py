import json
from pathlib import Path


def find_card(title, cards_list):
    """
    Ищет карточку по точному названию без учёта регистра и пробелов по краям.
    Получает строку title и список карточек cards_list, возвращает словарь или None.
    """
    query = title.strip().casefold()
    if query == "":
        return None

    for card in cards_list:
        if card["название"].strip().casefold() == query:
            return card
    return None


if __name__ == "__main__":
    cards_path = Path(__file__).parent.parent / "aleksandr" / "cards.json"
    with open(cards_path, "r", encoding="utf-8") as file:
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
