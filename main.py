import tkinter as tk
import pandas
import random
from tkinter import messagebox
import sys

BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pandas.read_csv(r"data\need_to_learn.csv")
    data_dict = data.to_dict(orient="records")
except (FileNotFoundError, pandas.errors.EmptyDataError):
    data = pandas.read_csv(r"data\french_words.csv")
    data_dict = data.to_dict(orient="records")
#Functions

def switch_button():
    language = canvas.itemcget(language_text, 'text')
    if language == "French":
        button_swap.config(command=flip_card_from_french)
        button_swap.invoke()
        button_swap.config(command=switch_button)
    elif language == "English":
        button_swap.config(command=flip_card_from_english)
        button_swap.invoke()
        button_swap.config(command=switch_button)
    
def remove_card():
    data_dict.remove(current_card)
    df = pandas.DataFrame(data_dict)
    df.to_csv(r"data\need_to_learn.csv", index=False)
    

def flip_card_from_english():
    canvas.itemconfig(image, image=flashcard_front)
    canvas.itemconfig(language_text, text = "French", fill = "black")
    canvas.itemconfig(flashcard_text, text=current_card.get("French"), fill = "black")
    
def flip_card_from_french():
    canvas.itemconfig(image, image=flashcard_back)
    canvas.itemconfig(language_text, text = "English", fill = "white")
    canvas.itemconfig(flashcard_text, text=current_card.get("English"), fill="white")
    
def next_card():
    try:
        global current_card
        global data_dict
        current_card = random.choice(data_dict)
        canvas.itemconfig(image, image=flashcard_front)
        canvas.itemconfig(language_text, text = "French", fill = "black")
        canvas.itemconfig(flashcard_text, text=current_card.get("French"), fill = "black")
    except IndexError:
        if messagebox.askyesno(title="Finished!", message="There are no cards left. Wanna learn again?"):
            data = pandas.read_csv(r"data\french_words.csv")
            data_dict = data.to_dict(orient="records")
        else:
            sys.exit(0)
#Setting up the UI.
screen = tk.Tk()
screen.title("Flash Cards")
screen.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

#Flash cards
canvas = tk.Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
flashcard_front = tk.PhotoImage(file=r"images\card_front.png")
flashcard_back = tk.PhotoImage(file=r"images\card_back.png")
image = canvas.create_image(400, 263, image = flashcard_front)
language_text = canvas.create_text(400, 150, text = "", font=("Roboto", "40", "italic"))
flashcard_text = canvas.create_text(400, 263, text = "", font=("Roboto", "60", "bold"))
canvas.grid(row = 0, column = 0, columnspan=3)

#Buttons
button_wrong_photo = tk.PhotoImage(file=r"images\wrong.png")
button_wrong = tk.Button(image=button_wrong_photo, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
button_wrong.grid(row=1, column=0)

button_right_photo = tk.PhotoImage(file=r"images\right.png")
button_right = tk.Button(image=button_right_photo, highlightthickness=0, bg=BACKGROUND_COLOR, command=lambda: [remove_card(), next_card()])
button_right.grid(row=1, column=2)

button_swap_card = tk.PhotoImage(file=r"images\swap.png")
language = canvas.itemcget(language_text, 'text')

button_swap = tk.Button(image=button_swap_card, highlightthickness=0, bg=BACKGROUND_COLOR, command=switch_button)
button_swap.grid(row=1, column=1)

next_card()
screen.mainloop()
