from tkinter import *
from tkinter import messagebox, simpledialog
# Dominik Matusiak, revelati00@gmail.com

def press():
    text = text_field.get(1.0, END)
    text_field.delete(1.0, END)
    text = text.upper()

    text2 = ""
    for a in range(len(text)):
        if text[a] == "A": text2 = text2+ "Z"
        if text[a] == "B": text2 = text2+ "Y"
        if text[a] == "C": text2 = text2+ "X"
        if text[a] == "D": text2 = text2+ "W"
        if text[a] == "E": text2 = text2+ "V"
        if text[a] == "F": text2 = text2+ "U"
        if text[a] == "G": text2 = text2+ "T"
        if text[a] == "H": text2 = text2+ "S"
        if text[a] == "I": text2 = text2+ "R"
        if text[a] == "J": text2 = text2+ "Q"
        if text[a] == "K": text2 = text2+ "P"
        if text[a] == "L": text2 = text2+ "O"
        if text[a] == "M": text2 = text2+ "N"
        if text[a] == "N": text2 = text2+ "M"
        if text[a] == "O": text2 = text2+ "L"
        if text[a] == "P": text2 = text2+ "K"
        if text[a] == "Q": text2 = text2+ "J"
        if text[a] == "R": text2 = text2+ "I"
        if text[a] == "S": text2 = text2+ "H"
        if text[a] == "T": text2 = text2+ "G"
        if text[a] == "U": text2 = text2+ "F"
        if text[a] == "V": text2 = text2+ "E"
        if text[a] == "W": text2 = text2+ "D"
        if text[a] == "X": text2 = text2+ "C"
        if text[a] == "Y": text2 = text2+ "B"
        if text[a] == "Z": text2 = text2+ "A"
        if text[a] == " ": text2 = text2+ " "
        if text[a] == ",": text2 = text2+ ","
        if text[a] == ".": text2 = text2+ "."
        if text[a] == ":": text2 = text2+ ":"
        if text[a] == "?": text2 = text2+ "?"
        if text[a] == "(": text2 = text2+ "("
        if text[a] == ")": text2 = text2+ ")"
        if text[a] == "/": text2 = text2+ "/"
        if text[a] == "-": text2 = text2+ "-"
        if text[a] == '"': text2 = text2+ '"'
        
    text_field.insert (1.0, text2)
                       
window = Tk()
window.geometry("500x360")
window.title("Ciper 1.0, Dominik Matusiak")

text_field = Text(window, width = 62, height = 20)
text_field.pack()
text_field.place(x=0, y=0)

butt = Button(window, text="Encode/Decode", width=20, height=1, command=press)
butt.pack()
butt.place(x=0, y=330)

window.mainloop()
