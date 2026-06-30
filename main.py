from tkinter import *

import pandas
import random

# words data
try:
    words_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    words_data = pandas.read_csv("data/french_words.csv")
words_data_list = words_data.to_dict(orient="records")

BACKGROUND_COLOR = "#B1DDC6"

shown_word = {}


def is_unknown():
    """Shows the next word on the card."""
    global shown_word, flip_timer
    window.after_cancel(flip_timer)
    # try:
    shown_word = random.choice(words_data_list)
    # except IndexError:
    #     messagebox.showinfo(title="We are finished.", message="You have learned all of the words in this application.")
    # else:
    canvas.itemconfig(bg_image, image=card_front)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=shown_word["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)


def is_known():
    global shown_word
    words_data_list.remove(shown_word)
    data = pandas.DataFrame(words_data_list)
    data.to_csv("data/words_to_learn.csv", index=False)
    is_unknown()
    print(len(data))
    # try:
    # except ValueError, IndexError:
    # else:


def flip_card():
    global shown_word
    canvas.itemconfig(bg_image, image=card_back)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=shown_word["English"], fill="white")


# window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# card front
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
bg_image = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)

# text
title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

# buttons
wrong_button_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=is_unknown)
wrong_button.grid(row=1, column=0)

right_button_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

is_unknown()

window.mainloop()
