import copy
import json
from pathlib import Path

from poisk import find_card


def main():
    cards_path = Path(__file__).resolve().parent.parent / "aleksandr" / "cards.json"
    with cards_path.open("r", encoding="utf-8") as file:
        cards = json.load(file)

    cards_snapshot = copy.deepcopy(cards)

    exact_cases = [
        ("FILE", "FILE"),
        ("GRAPH", "GRAPH"),
        ("DIAGNOSIS", "DIAGNOSIS"),
        ("file", "FILE"),
        (" FILE ", "FILE"),
        ("FIL", None),
        ("", None),
        ("ZZZ", None),
    ]

    print("=== Проверка точного поиска ===")
    for query, expected in exact_cases:
        result = find_card(query, cards)
        actual = result["название"] if result is not None else None
        assert actual == expected, f"Ошибка для {query!r}: ожидалось {expected!r}, получено {actual!r}"
        print(f"Запрос: {query!r} -> Ожидалось: {expected!r} -> Получено: {actual!r}")

    natural_language_cases = [
        ("как удалить график", "FILE"),
        ("аварийные сообщения", "DIAGNOSIS"),
    ]

    print("\n=== Проверка запросов своими словами (ограничение точного поиска) ===")
    for query, expected_by_meaning in natural_language_cases:
        result = find_card(query, cards)
        actual = result["название"] if result is not None else None
        assert result is None, f"Ожидалось None для {query!r}, получено {actual!r}"
        print(
            f"Запрос: {query!r} -> По смыслу: {expected_by_meaning!r} -> Получено: {actual!r} "
            "(ожидаемое ограничение точного поиска)"
        )

    assert cards == cards_snapshot, "Исходный список карточек был изменён!"
    print("\nСписок cards_list не изменён. Все проверки пройдены успешно.")


if __name__ == "__main__":
    main()
