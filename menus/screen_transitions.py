import app_functions as af
import ttkbootstrap as ttk
import menus.main_menu as mmenu
import menus.marking_menu as markm
import menus.quiz_creation as qc
import menus.quiz_menu as qm

def gotoQuizCreation(app : ttk.Window):
    af.clearWindow(app)
    qc.drawQuizCreator(app)

def gotoQuiz(app : ttk.Window):
    af.clearWindow(app)
    #NUMBER OF QUESTIONS IS CURRENTLY HERE
    qm.initQuiz(app, 10)


def gotoMarkingMenu(app : ttk.Window):
    af.clearWindow(app)
    markm.drawMarkingMenu(app)

def gotoMainMenu(app : ttk.Window):
    af.clearWindow(app)
    mmenu.drawMenu(app)