import tkinter as tk


def check_input():
    text = entry.get().strip()

    # Очищаем карточку перед каждым нажатием
    card_name.config(text="")
    card_answer.config(text="")
    card_doc.config(text="")
    card_page.config(text="")

    if not text:
        input_label.config(text="Введите запрос")
        return

    input_label.config(text=f"Вы ввели: {text}")

    # Заполняем карточку данными после нажатия кнопки
    card_name.config(text="Название: DIAGNOSIS")
    card_answer.config(text="Ответ: отображение аварийных сообщений")
    card_doc.config(text="Документ: Prilizhenie po KEDM.pdf")
    card_page.config(text="Страница: 6")


root = tk.Tk()
root.title("Помощник оператора — учебный пример")
root.geometry("500x520")

# --- Поле ввода и подпись «Запрос» ---
tk.Label(root, text="Запрос:").pack(anchor="w", padx=10, pady=(10, 0))

entry = tk.Entry(root, width=40)
entry.pack(padx=10, pady=5)

# --- Кнопка: подключение обработчика через command (имя без скобок) ---
btn = tk.Button(root, text="Ввод", command=check_input)
btn.pack(pady=10)

# --- Надпись под кнопкой, куда выводится введённый текст ---
input_label = tk.Label(root, text="Здесь появится то, что вы ввели",
                       wraplength=460, justify="left")
input_label.pack(anchor="w", padx=10)

# --- Отдельный заголовок для учебной карточки ---
tk.Label(root, text="Пример ответа:", font=("Arial", 11, "bold")).pack(
    anchor="w", padx=10, pady=(15, 0)
)

# --- Карточка DIAGNOSIS: размещается сразу, но строки пустые ---
card = tk.Frame(root, borderwidth=1, relief="solid", padx=10, pady=8)
card.pack(fill="x", padx=10, pady=5)

card_name = tk.Label(card, text="", anchor="w", justify="left", wraplength=440)
card_name.pack(anchor="w")

card_answer = tk.Label(card, text="", anchor="w", justify="left", wraplength=440)
card_answer.pack(anchor="w")

card_doc = tk.Label(card, text="", anchor="w", justify="left", wraplength=440)
card_doc.pack(anchor="w")

card_page = tk.Label(card, text="", anchor="w", justify="left")
card_page.pack(anchor="w")

root.mainloop()