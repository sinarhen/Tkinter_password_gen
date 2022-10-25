import tkinter as tk
from tkinter import ttk
from random import choice
from string import ascii_letters, digits


def generate(label):
    symbols = ascii_letters + digits
    passw = ''
    for i in range(15):
        passw += choice(symbols)
    label.config(text=passw)
    label.pack()


app = tk.Tk()
app.title('TITLE')
app.geometry('400x300')

label1 = ttk.Label(app, text='password')
btn = ttk.Button(app, text='Generate', command=lambda: generate(label1))
btn.pack()

app.mainloop()

