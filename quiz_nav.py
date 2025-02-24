import tkinter as tk
import quiz_gui as qgui
import ttkbootstrap as ttk
import quiz_objects as qobj
import custom_quiz as cq

#will probably need to mvoe this function later
def clearWindow(app: ttk.Window):
    #clears all widgets on the window
    widgets = app
    for w in app.winfo_children():
        w.pack_forget()

def getSelectedGobj(quiz : qobj.Quiz):
    #redefines which vertices were selected
        for selected_vertex in quiz.questions[quiz.current_question].graph.selected_vertices:
            for vertex in quiz.questions[quiz.current_question].graph.vertices:
                if selected_vertex == vertex:
                    vertex.state = True

        #redefines which edges were selected
        for selected_edge in quiz.questions[quiz.current_question].graph.selected_edges:
            for edge in quiz.questions[quiz.current_question].graph.edges:
                if selected_edge == edge:
                    edge.state = True

def drawQuizScreen(app : ttk.Window, quiz : qobj.Quiz):
    win_width = app.winfo_screenwidth()
    win_height = app.winfo_screenheight()

    CANV_W = int(win_width // 2.25)
    CANV_H = int(win_height - (win_height // 4) )

    #create initial gui
    gui_elements = qgui.initGraphGui(app,CANV_W, CANV_H)

    canv = gui_elements[0]
    right_frame = gui_elements[1]

    #random generation (for testing)
    #v_list = ggen.generateRandomVertices(CANV_W,CANV_H, 24)
    #e_list = ggen.generateRandomEdges(v_list, 1, 20)

    #current question
    current_question = quiz.current_question

    #create graph obj
    graph = quiz.questions[current_question].graph

    qgui.drawGraph(app,graph,canv,quiz,right_frame)

def nextQuestion(app : ttk.Window, quiz : qobj.Quiz):
    #there is a slight delay between clearing the screen and drawing new objects.
    #this could be made less noticeable by updating only the text and graph as opposed to all of
    #the frames and buttons, but this is not a priority.

    #if not on last question, increment to go to next question
    if quiz.current_question != quiz.num_questions:
        quiz.current_question += 1

        #clears the window, then redraws the screen with the new current question
        clearWindow(app)
        getSelectedGobj(quiz)
        drawQuizScreen(app, quiz)

        
    
    #if on last question
    else:
        raise Exception('Reached end of questions.')
    

def prevQuestion(app : ttk.Window, quiz : qobj.Quiz):
    #there is a slight delay between clearing the screen and drawing new objects.
    #this could be made less noticeable by updating only the text and graph as opposed to all of
    #the frames and buttons, but this is not a priority.

    #if not on first question, increment to go to next question
    if quiz.current_question != 1:
        quiz.current_question -= 1

        #clears the window, then redraws the screen with the new current question
        clearWindow(app)
        getSelectedGobj(quiz)
        drawQuizScreen(app, quiz)
    
    #nothing happens if on first question - button will do nothing.
    
    
    

    
