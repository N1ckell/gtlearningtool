import tkinter as tk
import ttkbootstrap as ttk
import menus.screen_transitions as st
import menus.quiz_func.quiz_objects as qobj

GUI_PADDING = 30
LABEL_PADDING = 20
INNER_PADDING = 5
FONT_SIZE = 'Calibri 30'
LIST_FONT = 'Calibri 20'

def drawMarkingMenu(app : ttk.Window, quiz : qobj.Quiz):
    menu_frame = tk.Frame(app)
    menu_frame.pack(expand = True, fill = 'both', padx = GUI_PADDING, pady = GUI_PADDING)

    #title
    ttk.Label(menu_frame, text= 'Quiz complete.', font = FONT_SIZE, justify = 'center').pack(padx = LABEL_PADDING, pady = LABEL_PADDING)

    #display list of marked questions
    list_marks = tk.Listbox(menu_frame, font = LIST_FONT, 
                            justify = 'center', takefocus=False)


    for i in range(1, quiz.num_questions + 1):
        str(quiz.questions[i].markQuestion())
        list_marks.insert(i, "Question " + str(i) + ": " + str(quiz.questions[i].markQuestion()) + ' out of ' + str(quiz.questions[i].marks) + ' marks')
        list_marks.pack(expand = True, fill = 'both', padx = GUI_PADDING, pady = LABEL_PADDING)
    

    #return to menu button
    btn_frame = tk.Frame(menu_frame)
    btn_frame.pack(fill = 'both',padx = GUI_PADDING, pady = GUI_PADDING, side='bottom')
    ttk.Button(btn_frame, text = 'Return to main menu', takefocus=False, command = lambda: st.gotoMainMenu(app)).pack(padx = GUI_PADDING, pady = INNER_PADDING, side = 'bottom')

