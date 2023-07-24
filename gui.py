import tkinter as tk
from tkinter import ttk
import random
from word_database import word_database

class TypingSpeedApp(tk.Frame):
    def __init__(self, master=None, check_space_func=None, word_limit=1):
        super().__init__(master)
        self.master = master
        self.master.title("Подсчет скорости печати")
        self.master.configure(bg="#262945")
        self.configure(bg="#262945")
        self.check_space_func = check_space_func  # Сохраняем переданную функцию check_space
        self.word_limit = word_limit  # Сохраняем переданное значение word_limit

        self.word_limit_label = tk.Label(self, text="Количество слов:", bg="#343d75", fg="lightblue", font=("Verdana", 12))
        self.word_limit_label.pack(pady=10)

        # Значения для выбора в выпадающем списке
        word_limit_values = [5, 10, 15, 20, 25, 50, 100]

        self.word_limit_combo = ttk.Combobox(self, values=word_limit_values, font=("Arial", 12), state="readonly")
        self.word_limit_combo.pack(pady=10)

        self.word_limit_combo.set(word_limit)

        self.text_label = tk.Label(self, text="Введите текст:",  bg="#343d75", fg="lightblue", font=("Verdana", 12))
        self.text_label.pack(pady=10)

        self.text_entry = tk.Text(self, height=15, bg="#606278", fg="white", font=("Verdana", 14))
        self.text_entry.pack(pady=10)

        self.start_button = tk.Button(self, text="Start typing", bg="#424453", fg="white", font=("Verdana", 12))
        self.start_button.pack(pady=10)

        self.end_button = tk.Button(self, text="Закончить печатать", bg="#3c4490", fg="white", font=("Verdana", 12))
        self.end_button.pack(pady=10)

        self.result_label = tk.Label(self, text="", bg="#262945", fg="white", font=("Verdana", 14))
        self.result_label.pack()

        self.word_label = tk.Label(self, text="", bg="#262945", fg="black", font=("Verdana", 14))
        self.word_label.pack()

        self.pack(anchor="center", padx=20, pady=60)  # Упаковываем главный контейнер

        self.text_entry.bind("<KeyRelease>", self.check_input)  # Привязываем обработчик события нажатия клавиши к текстовому полю
        self.text_entry.bind("<Key>", self.check_space)  # Привязываем обработчик события нажатия клавиши к текстовому полю

        self.current_word = ""

    def get_random_word(self):
        return random.choice(word_database)

    def update_word_label(self):
        random_word = self.get_random_word()
        self.word_label.configure(text=random_word, bg="#262945", fg="white", font=("Verdana", 14))

    def check_input(self, event):
        user_input = self.text_entry.get("1.0", tk.END).strip()
        for i, char in enumerate(user_input):
            if i >= len(self.current_word):
                break
            if char != self.current_word[i]:
                self.text_entry.tag_add("mistake", f"1.{i}", f"1.{i + 1}")
                self.text_entry.tag_configure("mistake", foreground="red")
                return
            else:
                self.text_entry.tag_remove("mistake", f"1.{i}", f"1.{i + 1}")
                return

    def check_space(self, event):
        if self.check_space_func:  # Проверяем, что функция check_space_func была передана
            self.check_space_func(event)  # Вызываем переданную функцию
