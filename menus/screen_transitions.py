import app_functions as af
import ttkbootstrap as ttk
import menus.main_menu as mmenu
import menus.marking_menu as markm
import menus.quiz_creation as qc
import menus.quiz_func.custom_quiz as cq
import menus.quiz_menu as qm
import menus.quiz_func.quiz_objects as qobj

def gotoQuizCreation(app : ttk.Window):
    af.clearWindow(app)
    qc.drawQuizCreator(app)

def gotoQuiz(app : ttk.Window, qno_selector : ttk.Combobox, qtype_selector : ttk.Combobox):
    af.clearWindow(app)

    num_questions = qno_selector.get()
    question_type = qtype_selector.get()

    #if the user selects out of combobox, it can be empty.
    #this stops the program from erroring  by instead using default values:
    if qno_selector.get() == '':
        num_questions = 5

    if qtype_selector.get() == '':
        question_type = "Include All"

    quiz = cq.generateQuiz(int(num_questions), question_type)
    qm.initQuiz(app, quiz)


def gotoMarkingMenu(app : ttk.Window, quiz : qobj.Quiz):
    af.clearWindow(app)
    markm.drawMarkingMenu(app, quiz)

def gotoMainMenu(app : ttk.Window):
    af.clearWindow(app)
    mmenu.drawMenu(app)