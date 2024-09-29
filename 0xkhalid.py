import tkinter as tk
from tkinter import scrolledtext as sc
import base64
import random
from tkinter import *

root = Tk()
root.geometry('970x560')
root.title('RedeemHub : Discord Token First Part : by 0xkhalid')

icon_image = PhotoImage(file='11zon_cropped.png')  
root.iconphoto(True, icon_image)

root.configure(background='black')

title = Label(root, text='Discord Token First Part : by 0xkhalid', font=('Courier', 18), bg='black', fg='white')
title.pack(fill=X)

canvas = Canvas(root, bg='black', highlightthickness=0)
canvas.place(x=0, y=0, width=970, height=560)

def scroll_numbers_bg():
    canvas.delete("all")
    for i in range(50):
        x_pos = random.randint(0, 970) 
        y_pos = random.randint(0, 560)
        numbers = ''.join([str(random.randint(0, 9)) for _ in range(10)])  # Random sequence of numbers
        canvas.create_text(x_pos, y_pos, text=numbers, fill='green', font=('Courier', 10, 'bold'))  # Draw numbers
    root.after(100, scroll_numbers_bg) 

def data():
    userid = en2.get()
    encodedBytes = base64.b64encode(userid.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")
    txt1.insert('end', 'Token First Part: ', 'red')
    txt1.insert('end', '\n')
    txt1.insert('end', encodedStr + '\n', 'red')
    txt1.insert('end', '\n')
    txt1.yview_moveto(1)


l2 = Label(root, text='ID:', fg='white', bg='black')
l2.place(x=130, y=40)

en2 = Entry(root, font=('Arial', 12), justify=CENTER, bd=0, relief='flat')
en2.place(x=40, y=59, width=150, height=30)
en2.configure(bg='gray', fg='white', insertbackground='white')  # Cursor color

button1 = Button(root, text='Start', width=25, height=2, cursor='hand2', command=data)
button1.place(x=4, y=480)  # Adjust the Y position to avoid overlap with the footer

button1.configure(bg='green', fg='white', font=('Arial', 12, 'bold'), relief='flat')

def on_enter(e):
    button1['bg'] = 'lime'

def on_leave(e):
    button1['bg'] = 'green'

button1.bind("<Enter>", on_enter)
button1.bind("<Leave>", on_leave)


txt1 = sc.ScrolledText(root, bg='black', fg='green')
txt1['font'] = ('Courier', 10, 'bold',)
txt1.place(x=200, y=35, width=750, height=500)
txt1.tag_config('red', background='black', foreground='red')
txt1.tag_config('gray', background='black', foreground='green')


footer_text = "type by 0xkhalid | redeem hub | Discord: 🔗 https://discord.gg/redeemhub"
footer_label = Label(root, text=footer_text, bg='black', fg='white', font=('Arial', 10))
footer_label.place(x=10, y=530)

scroll_numbers_bg()


root.mainloop()
