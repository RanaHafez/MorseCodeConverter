from tkinter import *
from morse_converter import *


window = Tk()
window.title("My Morse Code Program .. ")
window.minsize(width=450, height=500)
window.config(bg='#FF7F50')
window.config(pady=20, padx=20)

canvas = Canvas(width=250, height=250)
photo = PhotoImage(file='images/morse-icon.png')
canvas.create_image(110, 110, image=photo)
canvas.config(bg='#FF7F50', highlightthickness=0)
canvas.grid(row=0, column=2)

text_label = Label(text="Enter your Text")
text_label.grid(row=1, column=0, columnspan=2)
text_label.config(bg='#FF7F50')

text_entry = Entry(width=35)
text_entry.grid(row=1, column=2, columnspan=2)

morse_label = Label(text="Your Morse Code .. ")
morse_label.grid(row=2, column=0, columnspan=2)
morse_label.config(bg='#FF7F50')

morse_entry = Entry(width=35)
morse_entry.grid(row=2, column=2, columnspan=2)


def to_morse_button():
    if morse_entry.get() != "":
        morse_entry.delete(0, len(morse_entry.get()))
    if text_entry.get() != "":
        message = text_entry.get()
        cipher = to_morse(message.upper())
        print(cipher)
        morse_entry.insert(0, cipher)
        text_entry.delete(0, len(text_entry.get()))


def from_morse_button():
    if text_entry.get() != "":
        text_entry.delete(0, len(text_entry.get()))
    if morse_entry.get() != "":
        cipher = morse_entry.get()
        message = from_morse(cipher)
        text_entry.insert(0, message)
        morse_entry.delete(0, len(morse_entry.get()))


encode_button = Button(text="Convert To Morse", command=to_morse_button, width=30)
encode_button.grid(column=2, row=3, columnspan=2)
encode_button.config(bg='#80aaff')
decode_button = Button(text="Back to Text", command=from_morse_button, width=30, bg='#e8b248')
decode_button.grid(column=2, row=4, columnspan=2)

window.mainloop()