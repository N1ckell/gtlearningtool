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

def gotoQuiz(app : ttk.Window, combobox : ttk.Combobox):
    af.clearWindow(app)
    quiz = cq.generateQuiz2(int(combobox.get()))
    qm.initQuiz(app, quiz)


def gotoMarkingMenu(app : ttk.Window, quiz : qobj.Quiz):
    af.clearWindow(app)
    markm.drawMarkingMenu(app, quiz)

def gotoMainMenu(app : ttk.Window):
    af.clearWindow(app)
    mmenu.drawMenu(app)