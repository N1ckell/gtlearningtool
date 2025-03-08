import tkinter as tk
import ttkbootstrap as ttk
import menus.screen_transitions as st

GUI_PADDING = 30
LABEL_PADDING = 20
INNER_PADDING = 5
FONT_SIZE = 'Calibri 30'

def drawMenu(app : ttk.Window):
    menu_frame = tk.Frame(app)
    menu_frame.pack(expand = True, padx = GUI_PADDING, pady = GUI_PADDING)

    ttk.Label(menu_frame, text= 'Graph Theory Learning\n and Practice Tool', font = FONT_SIZE, justify = 'center').pack(padx = LABEL_PADDING, pady = LABEL_PADDING)

    btn_frame = tk.Frame(menu_frame)
    btn_frame.pack(expand = 'y', padx = GUI_PADDING, pady = GUI_PADDING)

    ttk.Button(btn_frame, text = 'Start a Quiz', takefocus=False, command = lambda: st.gotoQuizCreation(app)).pack(padx = GUI_PADDING, pady = INNER_PADDING, fill='both')
    ttk.Button(btn_frame, takefocus=False, text = 'Walkthrough Mode').pack(padx = GUI_PADDING, pady = INNER_PADDING, fill='both')
    ttk.Button(btn_frame, takefocus=False, text = 'Exit').pack(padx = GUI_PADDING, pady = INNER_PADDING, fill='both')
