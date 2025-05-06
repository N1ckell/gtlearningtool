
import ttkbootstrap as ttk
import menus.quiz_func.custom_quiz as cq
import menus.quiz_func.quiz_nav as qnav
import menus.quiz_func.quiz_objects as qobj

GUI_PADDING = 30
LABEL_PADDING = 20
INNER_PADDING = 5
FONT_SIZE = 'Calibri 30'

WINDOW_BG = 'lightgrey'


def initQuiz(app : ttk.Window, quiz : qobj.Quiz):
    
    qnav.drawQuizScreen(app, quiz)


