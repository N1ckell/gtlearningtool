import tkinter as tk
import ttkbootstrap as ttk
import graph_generation as ggen
import graph_gui as ggui
import custom_graph as cg
import custom_quiz as cq

import time as t

WINDOW_BG = 'lightgrey'

#create app window
app = ttk.Window(title= 'GT Learning Tool')
app.config(background = WINDOW_BG)
#starts the window maximised
app.state('zoomed')

win_width = app.winfo_screenwidth()
win_height = app.winfo_screenheight()

def clearWindow(app: ttk.Window):
    #clears all widgets on the window
    widgets = app
    for w in app.winfo_children():
        w.pack_forget()

def displayQuizScreen():

    CANV_W = int(win_width // 2.25)
    CANV_H = int(win_height - (win_height // 4) )

    #create initial gui
    gui_elements = ggui.initGraphGui(app,CANV_W, CANV_H)

    canv = gui_elements[0]
    right_frame = gui_elements[1]

    #random generation (for testing)
    #v_list = ggen.generateRandomVertices(CANV_W,CANV_H, 24)
    #e_list = ggen.generateRandomEdges(v_list, 1, 20)

    #create quiz obj
    quiz = cq.custom_quiz

    #current question
    current_question = quiz.current_question

    #create graph obj
    print(quiz.questions[1].graph)
    graph = quiz.questions[current_question].graph

    #draw and get mapping
    graph.e_map = ggen.drawEdges(canv, graph.edges)
    graph.v_map = ggen.drawVertices(canv, graph.vertices)

    #create gui labels
    ggui_labels = ggui.createGraphGui(app, graph, right_frame, canv, quiz)

    #bind canvas objects to corresponding click functions
    ggen.bindShapetoObj(canv, graph, ggui_labels)

displayQuizScreen()

app.mainloop()