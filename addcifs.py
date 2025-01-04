import sv_ttk
import easygui
import sys
import tkinter
from tkinter import ttk, StringVar, IntVar
from time import sleep


root = tkinter.Tk()

addcifs_header_label = ttk.Label(root, text="Add Cifs GUI")
addcifs_header_label.pack()

ip_label = ttk.Label(root, text="IP:")
ip_label.place(relx = 0.1, rely = 0.1, anchor = tkinter.CENTER)
ip_var = StringVar()
ip_var.set("default_text")
ip_entry = ttk.Entry(root, textvariable=ip_var)
ip_entry.place(relx = 0.5, rely = 0.1, anchor = tkinter.CENTER)

cifs_share_label = ttk.Label(root, text="Cifs Share:")
cifs_share_label.place(relx = 0.1, rely = 0.18, anchor = tkinter.CENTER)
cifs_share_var = StringVar()
cifs_share_var.set("default_text")
cifs_share_entry = ttk.Entry(root, textvariable=cifs_share_var)
cifs_share_entry.place(relx = 0.5, rely = 0.18, anchor = tkinter.CENTER)

local_path_label = ttk.Label(root, text="Local Path:")
local_path_label.place(relx = 0.1, rely = 0.26, anchor = tkinter.CENTER)
local_path_var = StringVar()
local_path_var.set("default_text")
local_path_entry = ttk.Entry(root, textvariable=local_path_var)
local_path_entry.place(relx = 0.5, rely = 0.26, anchor = tkinter.CENTER)

cifs_creds_label = ttk.Label(root, text="Cifs Creds:")
cifs_creds_label.place(relx = 0.1, rely = 0.34, anchor = tkinter.CENTER)
cifs_creds_var = StringVar()
cifs_creds_var.set("default_text")
cifs_creds_entry = ttk.Entry(root, textvariable=local_path_var)
cifs_creds_entry.place(relx = 0.5, rely = 0.34, anchor = tkinter.CENTER)

create_path_state = IntVar()
create_path_checkbox = ttk.Checkbutton(root, text = "Create Path", variable=create_path_state)
create_path_checkbox.place(relx = 0.05, rely = 0.42, anchor = tkinter.W)

add_to_fstab_state = IntVar()
add_to_fstab_checkbox = ttk.Checkbutton(root, text = "Add to FSTAB", variable=add_to_fstab_state)
add_to_fstab_checkbox.place(relx = 0.05, rely = 0.52, anchor = tkinter.W)

sv_ttk.set_theme("dark")

root.mainloop()
