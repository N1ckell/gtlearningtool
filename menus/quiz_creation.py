import tkinter as tk
import ttkbootstrap as ttk
import menus.screen_transitions as st
import menus.quiz_func.quiz_objects as qobj
import menus.quiz_func.custom_quiz as cq

GUI_PADDING = 30
LABEL_PADDING = 20
INNER_PADDING = 5
FONT_SIZE = 'Calibri 30'
SUBTITLE_FONT = 'Calibri 20'

WINDOW_BG = 'lightgrey'


def drawQuizCreator(app : ttk.Window):
    menu_frame = tk.Frame(app)
    menu_frame.pack(expand = True, fill = 'both', padx = GUI_PADDING, pady = GUI_PADDING)

    ttk.Label(menu_frame, text= 'Quiz Creation', font = FONT_SIZE, justify = 'center').pack(padx = LABEL_PADDING, pady = LABEL_PADDING)

    btn_frame = tk.Frame(menu_frame)
    btn_frame.pack(fill = 'both',padx = GUI_PADDING, pady = GUI_PADDING, side='bottom')

    ######################
    #   GET QUIZ INPUTS
    ######################


    ##  question number

    ttk.Label(menu_frame, text = 'Number of Questions:', font = SUBTITLE_FONT, ).pack(padx = LABEL_PADDING, pady=LABEL_PADDING)
    qno_txt = tk.StringVar()
    qno_txt.set('5')
    qno_selector = ttk.Combobox(menu_frame, state='readonly', takefocus=False, textvariable=qno_txt)
    qno_selector['values'] = ('5','10','20','30')
    qno_selector.current(0)
    qno_selector.pack(padx = GUI_PADDING + GUI_PADDING, pady=LABEL_PADDING)

    ######################

    ##  question type

    ttk.Label(menu_frame, text = 'Question Type:', font = SUBTITLE_FONT, ).pack(padx = LABEL_PADDING, pady=LABEL_PADDING)
    qtype_txt = tk.StringVar()
    qtype_txt.set('Include All')
    qtype_selector = ttk.Combobox(menu_frame, state='readonly', takefocus=False, textvariable=qtype_txt)
    qtype_selector['values'] = ("Include All", "Prim's Algorithm", "Kruskal's Algorithm")
    qtype_selector.current(0)
    qtype_selector.pack(padx = GUI_PADDING + GUI_PADDING, pady=LABEL_PADDING)

    ######################

    ttk.Button(btn_frame, text = 'Create quiz', takefocus=False, command = lambda: st.gotoQuiz(app, qno_selector, qtype_selector)).pack(padx = GUI_PADDING, pady = INNER_PADDING, side = 'bottom')



