import tkinter as tk
import ttkbootstrap as ttk
import menus.screen_transitions as st

GUI_PADDING = 30
LABEL_PADDING = 20
INNER_PADDING = 5
FONT_SIZE = 'Calibri 30'

def drawMarkingMenu(app : ttk.Window):
    menu_frame = tk.Frame(app)
    menu_frame.pack(expand = True, fill = 'both', padx = GUI_PADDING, pady = GUI_PADDING)

    ttk.Label(menu_frame, text= 'Quiz complete.', font = FONT_SIZE, justify = 'center').pack(padx = LABEL_PADDING, pady = LABEL_PADDING)

    btn_frame = tk.Frame(menu_frame)
    btn_frame.pack(fill = 'both',padx = GUI_PADDING, pady = GUI_PADDING, side='bottom')

    ttk.Button(btn_frame, text = 'Return to main menu', command = lambda: st.gotoMainMenu(app)).pack(padx = GUI_PADDING, pady = INNER_PADDING, side = 'bottom')

