import sv_ttk
import easygui
import sys
import tkinter
from tkinter import ttk


root = tkinter.Tk()

addcifs_header_label = ttk.Label(root, text="Add Cifs GUI", font="44")
addcifs_header_label.pack()

# button = ttk.Button(root, text="Click me!")
# button.pack()

# This is where the magic happens
sv_ttk.set_theme("dark")

root.mainloop()
