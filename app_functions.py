import tkinter as tk
import ttkbootstrap as ttk


def clearWindow(app: ttk.Window):
    #clears all widgets on the window
    for w in app.winfo_children():
        w.pack_forget()