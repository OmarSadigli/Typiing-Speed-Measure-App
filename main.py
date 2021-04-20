from tkinter import *
import math
from words import words
import random

# --------------- CONSTANTS --------------- #
TEXT_COLOR = "#ff7a00"
BG_COLOR = "#ffefcf"
timer_ = None
wpm = 0
current_high_score = 0
random_word = random.choice(words)


def word_counter(*args):
    global wpm, random_word
    if text_area.get() == random_word:
        wpm += 1
        score_label.config(text=f"WPM: {wpm}")
        text_area.delete(0,'end')
        random_word = random.choice(words)
        word_label.config(text=random_word)

    if text_area.get() != random.choice(words):
        wpm = wpm
        text_area.delete(0,'end')
        random_word = random.choice(words)
        word_label.config(text=random_word)


def start_timer(*args):
    global seconds
    seconds = 1 * 60
    count_down(seconds)


def count_down(count):
    global wpm, current_high_score
    word_label.config(fg="#ee7d3b")
    score_label.config(fg="#fbc518")
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    timer_label.config(text=f"Time Left\n0{count_min}:{count_sec}", fg="#fbc518")
    if count > 0:
        global timer_
        timer_ = window.after(1000,count_down,count - 1)
    else:
        word_label.config(text="TIME IS UP !!!", fg="#F72704")
        text_area.delete(0, "end")
        text_area.config(state="disabled")
        score_label.config(text=f"{wpm} WORDS\nPER MINUTE", fg='#FB543A')
        timer_label.config(fg="#FB543A")
        if wpm > current_high_score:
            current_high_score = wpm
        highest_score_label.config(text=f"Highest Score\n{current_high_score}")


# --------------- RESET --------------- #
def reset(*args):
    global wpm, random_word
    wpm = 0
    text_area.delete(0, "end")
    score_label.config(text=f"WPM: {wpm}")
    window.after_cancel(timer_)
    timer_label.config(text=f"Time Left\n00:00")
    window.focus_set()
    text_area.config(state="normal")
    random_word = random.choice(words)
    word_label.config(text=random_word)

    if text_area.get() == random_word:
        wpm += 1
        score_label.config(text=f"WPM: {wpm}")
        text_area.delete(0, 'end')
        random_word = random.choice(words)
        word_label.config(text=random_word)

    if text_area.get() != random.choice(words):
        wpm = wpm
        text_area.delete(0, 'end')
        random_word = random.choice(words)
        word_label.config(text=random_word)



# --------------- UI --------------- #
window = Tk()
window.title("Speedy Typer")
window.geometry("850x450")
window.config(bg=BG_COLOR,padx=45,pady=25)


canvas = Canvas(height=150,width=150,bg=BG_COLOR,highlightthickness=0)
logo_img = PhotoImage(file='keyboard.png')
canvas.create_image(50, 50, image=logo_img)
canvas.grid(row=0,column=0)

word_label = Label(window,text=random_word, font=("Courier",25,"bold"),bg=BG_COLOR,fg=TEXT_COLOR)
word_label.grid(row=0,column=1)

text_area = Entry(font=("Courier",14,"bold"),fg=TEXT_COLOR,bg=BG_COLOR,insertbackground=TEXT_COLOR,justify='center')
text_area.bind("<Return>", word_counter)
text_area.bind("<1>", start_timer)
text_area.grid(row=1, column=1, pady=50, padx=55)

score_label = Label(window, text=f"WPM: {wpm}",font=("Courier",18,"bold"),bg=BG_COLOR,fg=TEXT_COLOR)
score_label.grid(row=1, column=0, padx=50)

highest_score_label = Label(window, text=f"Highest Score\n{wpm}",font=("Courier",14,"bold"),bg=BG_COLOR,fg='#ca4533')
highest_score_label.place(x=600, y=-2)

timer_label = Label(window,text="Time Left\n00:00",font=("Courier",18,"bold"),bg=BG_COLOR,fg=TEXT_COLOR)
timer_label.grid(row=1, column=2)

restart_button = Button(window, text="Restart", font=("Courier",14,"bold"),bg=BG_COLOR,fg=TEXT_COLOR, command=reset, width=8)
restart_button.grid(row=3, column=1)

window.mainloop()
