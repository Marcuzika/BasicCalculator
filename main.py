from operator import length_hint
from tkinter import *
from tkinter import ttk
from turtle import width

# Colors
black = '#1c1c1b'
white = '#ffffff'
orange = '#FFAB40'
blue = '#38576b'

# Window
window = Tk()
window.title("Calculator")
window.geometry("235x340")
window.resizable(0, 0)

# Frames
display = Frame(window, width=235, height=50, bg=blue)
display.grid(row=0, column=0)

keyboard = Frame(window, width=235, height=298, bg=black)
keyboard.grid(row=1, column=0)

# Variable
value = ''

display_value = StringVar()
display_value.set("Drink water!")

# Fuctions


def show(n):
    global value
    value += n
    display_value.set(value)


def calculate():
    global value
    result = str(eval(value))
    value = result
    display_value.set(result)


def clean():
    global value
    value = ""
    display_value.set("")


# Label
display_label = Label(display, textvariable=display_value, width=16,
                      height=2, anchor="e", font=('Ivy 18'), bg=blue, fg=white)
display_label.place(x=0, y=0)

footer = Label(keyboard, text='© Zika Labs.', bg=black,
               fg=white, font=('Ivy 11 italic'))
footer.place(x=73, y=263)

# Buttons:

# 1º row
b_c = Button(keyboard, command=clean, text="C", width=12, height=2, font=(
    'Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_c.place(x=0, y=0)

b_perc = Button(keyboard, command=lambda: show("%"), text="%", width=6, height=2, font=(
    'Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_perc.place(x=118, y=0)

b_bar = Button(keyboard, command=lambda: show("/"), text="/", width=6, height=2, bg=orange, fg=white,
               font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_bar.place(x=176, y=0)

# 2º row
b_7 = Button(keyboard, command=lambda: show("7"), text="7", width=6, height=2, font=(
    'Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=0, y=52)

b_8 = Button(keyboard, command=lambda: show("8"), text="8", width=6, height=2, font=(
    'Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=59, y=52)

b_9 = Button(keyboard, command=lambda: show("9"), text="9", width=6, height=2, font=(
    'Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=118, y=52)

b_mult = Button(keyboard, command=lambda: show("*"), text="*", width=6, height=2, bg=orange, fg=white,
                font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_mult.place(x=177, y=52)

# 3º row
b_4 = Button(keyboard, command=lambda: show("4"), text="4", width=6, height=2, font=(
    'Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=104)

b_5 = Button(keyboard, command=lambda: show("5"), text="5", width=6, height=2, font=(
    'Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=104)

b_6 = Button(keyboard, command=lambda: show("6"), text="6", width=6, height=2, font=(
    'Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=104)

b_sub = Button(keyboard, command=lambda: show("-"), text="-", width=6, height=2, bg=orange, fg=white,
               font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_sub.place(x=177, y=104)

# 4º row
b_1 = Button(keyboard, command=lambda: show("1"), text="1", width=6, height=2, font=(
    'Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=156)

b_2 = Button(keyboard, command=lambda: show("2"), text="2", width=6, height=2, font=(
    'Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=59, y=156)

b_3 = Button(keyboard, command=lambda: show("3"), text="3", width=6, height=2, font=(
    'Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=118, y=156)

b_add = Button(keyboard, command=lambda: show("+"), text="+", width=6, height=2, bg=orange, fg=white,
               font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_add.place(x=177, y=156)

# 5º row
b_0 = Button(keyboard, command=lambda: show("0"), text="0", width=12, height=2, font=(
    'Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_0.place(x=0, y=208)

b_dot = Button(keyboard, command=lambda: show("."), text=".", width=6, height=2, font=(
    'Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_dot.place(x=118, y=208)

b_eq = Button(keyboard, command=calculate, text="=", width=6, height=2, bg=orange, fg=white,
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_eq.place(x=177, y=208)

window.mainloop()
