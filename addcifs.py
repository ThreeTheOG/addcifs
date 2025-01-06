import sv_ttk
import easygui
import sys
import tkinter
from tkinter import ttk, StringVar, IntVar
from tktooltip import ToolTip
# from os import geteuid

# uid = geteuid()
# if uid != 0:
#     print('UID not 0, please run as root or with sudo.')
#     exit()

root = tkinter.Tk()

root.geometry('375x500')
root.resizable(False, False)
root.attributes('-type', 'dialog')

addcifs_header_label = ttk.Label(root, text="Add Cifs GUI")
addcifs_header_label.pack()

ip_label = ttk.Label(root, text="IP:")
ip_label.place(relx = 0.1, rely = 0.1, anchor = tkinter.CENTER)
ip_var = StringVar()
ip_var.set("default_text")
ip_entry = ttk.Entry(root, textvariable=ip_var)
ip_entry.place(relx = 0.5, rely = 0.1, anchor = tkinter.CENTER)
ToolTip(ip_entry, msg = "The IP of the CIFS server. (Ex: 10.0.0.111)")

cifs_share_label = ttk.Label(root, text="Cifs Share:")
cifs_share_label.place(relx = 0.13, rely = 0.18, anchor = tkinter.CENTER)
cifs_share_var = StringVar()
cifs_share_var.set("default_text")
cifs_share_entry = ttk.Entry(root, textvariable=cifs_share_var)
cifs_share_entry.place(relx = 0.5, rely = 0.18, anchor = tkinter.CENTER)
ToolTip(cifs_share_entry, msg = "Cifs Share Path. (Ex: /my_share)")

local_path_label = ttk.Label(root, text="Local Path:")
local_path_label.place(relx = 0.13, rely = 0.26, anchor = tkinter.CENTER)
local_path_var = StringVar()
local_path_var.set("default_text")
local_path_entry = ttk.Entry(root, textvariable=local_path_var)
local_path_entry.place(relx = 0.5, rely = 0.26, anchor = tkinter.CENTER)
ToolTip(local_path_entry, msg = "The local path of the share (Ex: /mnt/my_share)")

cifs_creds_label = ttk.Label(root, text="Cifs Creds:")
cifs_creds_label.place(relx = 0.13, rely = 0.34, anchor = tkinter.CENTER)
cifs_creds_var = StringVar()
cifs_creds_var.set("default_text")
cifs_creds_entry = ttk.Entry(root, textvariable=local_path_var)
cifs_creds_entry.place(relx = 0.5, rely = 0.34, anchor = tkinter.CENTER)
ToolTip(cifs_creds_entry, msg = "The path of your SMB Credentials file. (Ex: /home/user/.smbcredentials)")

create_path_state = IntVar()
create_path_checkbox = ttk.Checkbutton(root, text = "Create Path", variable=create_path_state)
create_path_checkbox.place(relx = 0.05, rely = 0.42, anchor = tkinter.W)
ToolTip(create_path_checkbox, msg = "Create path on execution.")

restart_systemd_daemon_state = IntVar()
restart_systemd_daemon_checkbox = ttk.Checkbutton(root, text = "Restart Systmed Daemon", variable=restart_systemd_daemon_state)
restart_systemd_daemon_checkbox.place(relx = 0.05, rely = 0.58, anchor = tkinter.W)

mount_all_state = IntVar()
mount_all_checkbox = ttk.Checkbutton(root, text = "Mount All", variable=mount_all_state)
mount_all_checkbox.place(relx = 0.05, rely = 0.66, anchor = tkinter.W)

def save_defaults(): pass

save_defaults_button = ttk.Button(root, text = "Save Defaults", command = save_defaults)
save_defaults_button.place(relx = 0.5, rely = 0.82, anchor = tkinter.CENTER)
ToolTip(save_defaults_button, msg = "Save defaults to file excluding cifs share/local path. (./.addcifs_defaults.json)")

def write(): pass

write_button = ttk.Button(root, text = "Write", command = write)
write_button.place(relx = 0.5, rely = 0.90, anchor = tkinter.CENTER)


sv_ttk.set_theme("dark")

root.mainloop()
