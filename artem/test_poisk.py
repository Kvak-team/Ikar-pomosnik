import json
from pathlib import Path

from poisk import find_card

cards_path = Path(__file__).parent.parent / "aleksandr" / "cards.json"
with open(cards_path, "r", encoding="utf-8") as file:
    cards = json.load(file)

tests = [
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
errors = 0

for query, expected in tests:
    result = find_card(query, cards)

    if result is None:
        actual = None
    else:
        actual = result["название"]

    if actual == expected:
        status = "ОК"
    else:
        status = "ОШИБКА"
        errors += 1

    print(f"[{status}] Ввод: '{query}' | Ожидалось: {expected} | Получено: {actual}")

print("\n=== Запросы своими словами (ограничение точного поиска) ===")
natural_queries = [
    ("как удалить график", "FILE"),
    ("аварийные сообщения", "DIAGNOSIS"),
]

for query, meaning in natural_queries:
    result = find_card(query, cards)

    if result is None:
        actual = None
    else:
        actual = result["название"]

    print(f"Ввод: '{query}' | По смыслу: {meaning} | Получено: {actual}")

with open(cards_path, "r", encoding="utf-8") as file:
    original_cards = json.load(file)

if cards == original_cards:
    print("\n[ОК] Исходный список карточек не изменился.")
else:
    print("\n[ОШИБКА] Исходный список карточек изменился!")
    errors += 1

print(f"\nИтог: ошибок = {errors}")
