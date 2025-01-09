#!/home/mt/Desktop/addcifs/venv/bin/python3

import sv_ttk
import easygui
import sys
import tkinter
from tkinter import ttk, StringVar, IntVar
from tktooltip import ToolTip
import os
import json
# from os import geteuid

# uid = geteuid()
# if uid != 0:
#     print('UID not 0, please run as root or with sudo.')
#     exit()

defaults_file_name = '.addcifs_defaults.json'
defaults_file_path = __file__[:-12] + defaults_file_name

root = tkinter.Tk()

root.geometry('375x500')
root.resizable(False, False)
# set window to float on TWM
root.attributes('-type', 'dialog')


# UI Vars
ip_var = StringVar() # input
cifs_share_var = StringVar() # input
local_path_var = StringVar() # input
cifs_creds_var = StringVar() # input
create_path_state = IntVar() # checkbox
restart_systemd_daemon_state = IntVar() # checkbox
mount_all_state = IntVar() # checkbox

inputs = [ip_var, cifs_share_var, local_path_var]
def check_empty(inputs: list): # returns True if empty
    for var in inputs:
        if var.get() == "":
            return True


def save_defaults():
    defaults_dict = {
        'ip': ip_var.get(),
        'cifs_credentials_file': cifs_creds_var.get(),
        'create_path_state': create_path_state.get(),
        'restart_daemon_state': restart_systemd_daemon_state.get(),
        'mount_all_state': mount_all_state.get()
    }

    f = open(defaults_file_path, 'w')
    f.write(json.dumps(defaults_dict, indent = 4))

def load_defaults():
    if os.path.exists(defaults_file_path):
        f = open(defaults_file_path, 'r')
        if f.read() != '':
            try:
                f.seek(0)
                json_dict = json.load(f)
            except json.JSONDecodeError as e:
                print(defaults_file_path)
                print(f'Invalid json data in {defaults_file_path}. Delete the file, or fix the error to resume. (Original Error: {e})')
                return

        ip_var.set(json_dict['ip'])
        cifs_creds_var.set(json_dict['cifs_credentials_file'])
        create_path_state.set(json_dict['create_path_state'])
        restart_systemd_daemon_state.set(json_dict['restart_daemon_state'])
        mount_all_state.set(json_dict['mount_all_state'])
load_defaults()

def write():
    if create_path_state.get() == 1:
        if not os.path.isdir(local_path_var.get()):
            os.makedirs(local_path_var.get())

    if restart_systemd_daemon_state.get() == 1:
        os.system('sudo systemctl --daemon-reload')

    if mount_all_state.get() == 1:
        os.system('sudo mount -a')


addcifs_header_label = ttk.Label(root, text="Add Cifs GUI")
addcifs_header_label.pack()

# Inputs
ip_label = ttk.Label(root, text="IP:")
ip_label.place(relx = 0.1, rely = 0.1, anchor = tkinter.CENTER)
# ip_var.set("default_text")
ip_entry = ttk.Entry(root, textvariable=ip_var)
ip_entry.place(relx = 0.5, rely = 0.1, anchor = tkinter.CENTER)
ToolTip(ip_entry, msg = "The IP of the CIFS server. (Ex: 10.0.0.111)")

cifs_share_label = ttk.Label(root, text="Cifs Share:")
cifs_share_label.place(relx = 0.13, rely = 0.18, anchor = tkinter.CENTER)
# cifs_share_var.set("default_text")
cifs_share_entry = ttk.Entry(root, textvariable=cifs_share_var)
cifs_share_entry.place(relx = 0.5, rely = 0.18, anchor = tkinter.CENTER)
ToolTip(cifs_share_entry, msg = "Cifs Share Path. (Ex: /my_share)")

local_path_label = ttk.Label(root, text="Local Path:")
local_path_label.place(relx = 0.13, rely = 0.26, anchor = tkinter.CENTER)
# local_path_var.set("default_text")
local_path_entry = ttk.Entry(root, textvariable=local_path_var)
local_path_entry.place(relx = 0.5, rely = 0.26, anchor = tkinter.CENTER)
ToolTip(local_path_entry, msg = "The local path of the share (Ex: /mnt/my_share)")

cifs_creds_label = ttk.Label(root, text="Cifs Creds:")
cifs_creds_label.place(relx = 0.13, rely = 0.34, anchor = tkinter.CENTER)
# cifs_creds_var.set("default_text")
cifs_creds_entry = ttk.Entry(root, textvariable=cifs_creds_var)
cifs_creds_entry.place(relx = 0.5, rely = 0.34, anchor = tkinter.CENTER)
ToolTip(cifs_creds_entry, msg = "The path of your SMB Credentials file. (Ex: /home/user/.smbcredentials)")


# Checkboxes
create_path_checkbox = ttk.Checkbutton(root, text = "Create Path", variable=create_path_state)
create_path_checkbox.place(relx = 0.03, rely = 0.42, anchor = tkinter.W)
ToolTip(create_path_checkbox, msg = "Create path on execution.")

restart_systemd_daemon_checkbox = ttk.Checkbutton(root, text = "Restart Systmed Daemon", variable=restart_systemd_daemon_state)
restart_systemd_daemon_checkbox.place(relx = 0.03, rely = 0.50, anchor = tkinter.W)

mount_all_checkbox = ttk.Checkbutton(root, text = "Mount All", variable=mount_all_state)
mount_all_checkbox.place(relx = 0.03, rely = 0.58, anchor = tkinter.W)


# Buttons
save_defaults_button = ttk.Button(root, text = "Save Defaults", command = save_defaults)
save_defaults_button.place(relx = 0.5, rely = 0.82, anchor = tkinter.CENTER)
ToolTip(save_defaults_button, msg = f"Save defaults to file excluding cifs share/local path. ({defaults_file_path})")

write_button = ttk.Button(root, text = "Write", command = write)
write_button.place(relx = 0.5, rely = 0.90, anchor = tkinter.CENTER)
ToolTip(write_button, msg = "Write to FSTAB.")


sv_ttk.set_theme("dark")

root.mainloop()
