import tkinter as tk
import ttkbootstrap as ttk

#will probably need to mvoe this function later
def clearWindow(app: ttk.Window):
    #clears all widgets on the window
    widgets = app
    for w in app.winfo_children():
        w.pack_forget()