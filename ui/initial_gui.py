from tkinter.constants import X, Y
from PIL import Image,ImageTk
from tkinter.font import BOLD
from tkinter import Widget, messagebox

import tkinter as tk
import server.s_dashboard as server
import client.c_dashboard as client

username_return = None
ip = None
port = None

def ip_port_window(username, window):
    if username == "":
        messagebox.showerror(title = "Errore", message = "Username non inserito")

    elif len(username) > 10:
        messagebox.showerror(title="Error", message = "L'username non può superare i 10 caratteri")

    else:    
        root = tk.Tk()
        root.resizable(False, False)
        root.geometry("200x225")
        root.configure(background = "#dbdbdb")

        tk.Label(root,
        text = "Ip",
        font = ("Verdana", 15, BOLD)
        ).place(x = 0, y = 0)

        entry_ip = tk.Entry(root, 
        width = 12, 
        font = ("Verdana", 15, BOLD)
        )
        
        entry_ip.place(x = 1, y = 40)

        tk.Label(root, 
        text = "Port", 
        font = ("Verdana", 15, BOLD)
        ).place(x = 0, y = 80)

        entry_port = tk.Entry(root,
        width = 12, 
        font = ("Verdana", 15, BOLD)
        )

        entry_port.place(x = 1, y = 120)

        tk.Button(root, 
        text = "Ok", 
        font = ("Verdana", 15, BOLD),
        background = "#dbdbdb",
        activebackground = "#dbdbdb"
        ).place(x = 75, y = 180)

        root.mainloop()

def convert_picture(path,size1,size2):

    img1 = Image.open(path)

    img2 = img1.resize((size1, size2), Image.ANTIALIAS)

    img3 = ImageTk.PhotoImage(img2)

    return img3

def create_chat(username,window):
    global username_return

    if username == "":
        messagebox.showerror(title = "Errore", message = "Username non inserito")

    elif len(username) > 10:
        messagebox.showerror(title = "Errore", message = "L'username non può superare i 10 caratteri")

    else:
        username_return = username
        window.destroy()
            
def initial_window():
    window = tk.Tk()
    window.geometry("500x400")
    window.resizable(False, False)
    window.configure(background = "#dbdbdb")

    logo_immagine = convert_picture("assets\\masta_chat.gif", 225, 225)

    tk.Label(window, image = logo_immagine,
        height = 50,
        width = 220,
        background = "#dbdbdb"
    ).place(x = 130, y = 70)

    tk.Button(window,
        text = "Crea", 
        width = 7, 
        height = 2, 
        font = ("Verdana", 13, BOLD), 
        activeforeground = "#000000",
        background = "#dbdbdb",
        activebackground = "#dbdbdb",
        command = lambda: create_chat (username = entry_username.get(),
                                      window = window
                                      )
        ).place(x = 145, y = 240)
        
    tk.Button(window,
        text = "Partecipa",
        width = 7,
        height = 2,
        font = ("Verdana", 13, BOLD),
        activeforeground = "#000000",
        background = "#dbdbdb",
        activebackground = "#dbdbdb",
        command = lambda: ip_port_window (username = entry_username.get(),
                                          window = window
                                         )
        ).place(x = 270, y = 240)
    
    entry_username = tk.Entry(window,
        background = "#ffffff",
        font = ("Verdana", 15, BOLD))

    entry_username.place(x = 115, y = 180)
    
    window.mainloop()

    return str(username_return)