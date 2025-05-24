import tkinter as tk
from tkinter import messagebox


class IceCreamStand:
    def __init__(self, root):
        self.root = root
        self.root.title("Кафе-мороженое")
        self.root.geometry("500x400")
        self.root.configure(bg="#FFF5E6")  # Кремовый фон

        # Основные данные
        self.name = "Сладкоежка"
        self.flavors = ["Ванильное", "Шоколадное", "Клубничное", "Фисташковое", "Мятное"]
        self.prices = {"Ванильное": 50, "Шоколадное": 60, "Клубничное": 55,
                       "Фисташковое": 70, "Мятное": 65}

        # интерфейс
        self.create_header()
        self.create_flavors_list()
        self.create_icecream_stand()
        self.create_controls()

    def create_header(self):
        # название
        header = tk.Frame(self.root, bg="#FF9966", height=60)
        header.pack(fill="x", padx=10, pady=10)

        tk.Label(header, text=self.name, font=("Comic Sans MS", 18, "bold"),
                 bg="#FF9966", fg="white").pack(pady=10)

    def create_flavors_list(self):
        # список мороженого
        list_frame = tk.Frame(self.root, bg="#FFF5E6")
        list_frame.pack(side="left", fill="both", expand=True, padx=10)

        tk.Label(list_frame, text="Наше меню:", font=("Arial", 12, "bold"),
                 bg="#FFF5E6").pack(anchor="w")

        self.listbox = tk.Listbox(list_frame, font=("Arial", 11),
                                  width=25, height=10, selectbackground="#FF9966")
        self.listbox.pack(fill="both", expand=True)

        # Добавляем сорта в список
        for flavor in self.flavors:
            self.listbox.insert("end", f"{flavor} - {self.prices[flavor]} руб.")

    def create_icecream_stand(self):
        # Холст с рисунком мороженого
        canvas = tk.Canvas(self.root, width=200, height=300, bg="#FFF5E6",
                           highlightthickness=0)
        canvas.pack(side="right", padx=10, pady=10)

        colors = {
            "Ванильное": "#FFFFF0",
            "Шоколадное": "#8B4513",
            "Клубничное": "#FF69B4",

        }

        # шарики
        y_pos = 180
        for flavor in self.flavors[:3]:  # Показываем первые 3 сорта
            canvas.create_oval(70, y_pos, 130, y_pos - 60, fill=colors[flavor], outline="black")
            y_pos -= 45
        # рожок
            canvas.create_polygon(100, 300, 50, 150, 150, 150, fill="#F4A460", outline="black")


    def create_controls(self):
        # Кнопки управления
        controls = tk.Frame(self.root, bg="#FFF5E6")
        controls.pack(fill="x", padx=0, pady=10)

        tk.Button(controls, text="Выбрать", command=self.select_flavor,
                  bg="#FF9966", fg="white").pack(side="left", padx=0)
        tk.Button(controls, text="Выход", command=self.root.quit,
                  bg="#FF9966").pack(side="right", padx=0)

    def select_flavor(self):
        try:
            selection = self.listbox.curselection()[0]
            flavor = self.flavors[selection]
            messagebox.showinfo("Выбор", f"Вы выбрали: {flavor}\nЦена: {self.prices[flavor]} руб.")
        except:
            messagebox.showwarning("Ошибка")


root = tk.Tk()
app = IceCreamStand(root)
root.mainloop()