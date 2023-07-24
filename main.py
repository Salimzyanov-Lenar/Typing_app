import time
import tkinter as tk
from gui import TypingSpeedApp
from main_logic import calculate_typing_speed

WORD_LIMIT = 5
word_count = 0

def start_typing(event=None):
    word_limit = int(app.word_limit_combo.get())  # Получаем значение из выпадающего списка
    app.text_entry.delete("1.0", tk.END)
    app.text_entry.configure(state=tk.NORMAL)  # Разрешаем редактирование текстового поля
    global start_time, word_count, WORD_LIMIT
    start_time = time.time()
    word_count = 0
    WORD_LIMIT = word_limit  # Обновляем значение глобальной переменной WORD_LIMIT
    app.update_word_label()  # Обновляем случайное слово


def end_typing(event):
    end_time = time.time()
    duration = end_time - start_time
    typing_speed = calculate_typing_speed(app.text_entry.get("1.0", tk.END), duration)
    app.result_label.configure(text="Скорость печати: {:.2f} слов в секунду.".format(typing_speed))
    app.text_entry.configure(state=tk.DISABLED)  ### TEST


def check_space(event):
    global word_count
    if event.keysym == "space":
        word_count += 1
        if word_count >= WORD_LIMIT:
            end_typing(None)  # Завершаем ввод после достижения лимита слов
        else:
            app.update_word_label()  # Обновляем случайное слово


if __name__ == "__main__":
    root = tk.Tk()  # Создаем главное окно Tkinter
    app = TypingSpeedApp(root, check_space, WORD_LIMIT)  # Создаем экземпляр класса TypingSpeedApp с передачей главного окна

    app.start_button.bind("<Button-1>", start_typing)
    app.end_button.bind("<Button-1>", end_typing)
    app.text_entry.bind("<Key>", check_space)

    app.text_entry.configure(state=tk.DISABLED)

    root.mainloop()
