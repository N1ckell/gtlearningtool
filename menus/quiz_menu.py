'''#create quiz obj
quiz = cq.generateQuiz1(10)

qnav.drawQuizScreen(app, quiz)'''

import ttkbootstrap as ttk
import menus.quiz_func.custom_quiz as cq
import menus.quiz_func.quiz_nav as qnav

GUI_PADDING = 30
LABEL_PADDING = 20
INNER_PADDING = 5
FONT_SIZE = 'Calibri 30'

WINDOW_BG = 'lightgrey'


def initQuiz(app : ttk.Window, no_questions : int):
    quiz = cq.generateQuiz1(no_questions)
    qnav.drawQuizScreen(app, quiz)


