BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import random
from pandas import *




# read csv and modify for one dataframe(planilha), use pandas for work datas
# data = read_csv("data/english.csv")

# read dataframe and modify to dictionary
# word_list = data.to_dict(orient="records")
words = {}
word_list = {}
try:
    data = read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = read_csv("data/english.csv")
    word_list = original_data.to_dict(orient="records")
else:
    word_list = data.to_dict(orient="records")

# esse orient records, transforma em uma lista de dicionarios



def new_translation():
    global  words, flip_timer, word_list
    window.after_cancel(flip_timer)
    words = random.choice(word_list)
    canvas.itemconfig(text_card, text="English", fill= "black")
    canvas.itemconfig(text_translation, text=words["English"], fill="black")
    canvas.itemconfig(image_now, image = logo_img)
    flip_timer = window.after(3000, func=timer_finish)

def is_know():
    word_list.remove(words)
    data = DataFrame(word_list)
    data.to_csv("words_to_learn.csv", index=False)
    new_translation()

def timer_finish():
    canvas.itemconfig(image_now, image= image_finish)
    canvas.itemconfig(text_card, text="Portugues", fill="white")
    canvas.itemconfig(text_translation, text=words["Portugues"], fill="white")

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg =BACKGROUND_COLOR)
flip_timer = window.after(3000, func=timer_finish)

image_finish = PhotoImage(file= "images/card_back.png")
canvas = Canvas(height=526, width=800)
logo_img = PhotoImage(file="images/card_front.png")
image_now = canvas.create_image(400, 263, image=logo_img)
canvas.config(bg = BACKGROUND_COLOR, highlightthickness=0)
text_card = canvas.create_text(400, 150, text="title", font=("Ariel", 40, "italic"))
text_translation = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column =0, columnspan =2)




image_right = PhotoImage(file="images/right.png")
right = Button(image=image_right, highlightthickness=0, command=is_know)
right.grid(row=1, column=1)

image_wrong = PhotoImage(file="images/wrong.png")
wrong = Button(image=image_wrong, highlightthickness=0, command=new_translation)
wrong.grid(row=1, column=0)





new_translation()






window.mainloop()