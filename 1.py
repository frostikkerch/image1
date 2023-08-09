import tkinter as tk
import requests
from PIL import Image, ImageTk
import io
import random

class ColorGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Generator")
        self.root.configure(bg="purple")

        self.create_widgets()

    def create_widgets(self):
        # Получение данных изображения из интернета
        image_url = "https://github.com/frostikkerch/image1/blob/main/210320231679371554.png?raw=true"
        response = requests.get(image_url)
        image_data = response.content

        # Создание изображения из данных
        image = Image.open(io.BytesIO(image_data))
        image = image.resize((800, 600), Image.LANCZOS)  # Размер по вашему усмотрению
        self.background_image = ImageTk.PhotoImage(image)

        # Вывод изображения с кнопкой внизу
        self.image_label = tk.Label(self.root, image=self.background_image, bg="white")
        self.image_label.pack()

        # Прямоугольник с экраном вывода цветов
        self.color_frame = tk.Frame(self.image_label, bg="white", bd=2)
        self.color_frame.place(relx=0.5, rely=0.35, anchor="center", relwidth=0.1, relheight=0.1)

        # Вывод цветов внутри экрана
        self.color_label = tk.Label(self.color_frame, text="", font=("Helvetica", 20), bg="white", fg="black")
        self.color_label.pack(pady=10)

        # Кнопка получения цвета с отступом от низа, большим размером и отступом вверх
        self.start_button = tk.Button(self.image_label, text="Получить", command=self.generate_color, bg="purple", fg="white", font=("Helvetica", 16))
        self.start_button.place(relx=0.5, rely=0.9, anchor="s", relwidth=0.6)  # Размещаем кнопку внизу изображения

    def generate_color(self):
        colors = ["green", "black", "red"]
        probabilities = [0.04, 0.48, 0.48]

        chosen_color = random.choices(colors, probabilities)[0]
        self.color_label.config(text=chosen_color, fg=chosen_color)

if __name__ == "__main__":
    root = tk.Tk()
    app = ColorGeneratorApp(root)
    root.mainloop()
