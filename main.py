import tkinter as tk
import csv

BACKGROUND_COLOR = "#B1DDC6"

#Setting up the UI.
screen = tk.Tk()
screen.title("Flash Cards")
screen.configure(bg=BACKGROUND_COLOR, padx=50, pady=50)

#Flash cards
canvas = tk.Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
flashcard_front = tk.PhotoImage(file=r"images\card_front.png")
canvas.create_image(400, 260, image = flashcard_front)
language_text = canvas.create_text(400, 150, text = "Title", font=("Roboto", "40", "italic"))
flashcard_text = canvas.create_text(400, 263, text = "Word", font=("Roboto", "60", "bold"))

canvas.grid(row = 0, column = 0, columnspan=2)

#Buttons
button_wrong_photo = tk.PhotoImage(file=r"images\wrong.png")
button_wrong = tk.Button(image=button_wrong_photo, highlightthickness=0, bg=BACKGROUND_COLOR)
button_wrong.grid(row=1, column=0)

button_right_photo = tk.PhotoImage(file=r"images\right.png")
button_right = tk.Button(image=button_right_photo, highlightthickness=0, bg=BACKGROUND_COLOR)
button_right.grid(row=1, column=1)

screen.mainloop()

