import tkinter as tk
import menus.quiz_func.quiz_gui as qgui
import ttkbootstrap as ttk
import menus.quiz_func.quiz_objects as qobj
import menus.screen_transitions as st
import app_functions as af

def kruskalsQuestion(question : qobj.Question):
    return isinstance(question, qobj.KruskalsQuestion)

def primsQuestion(question : qobj.Question):
    return isinstance(question, qobj.PrimsQuestion)

def clearGraphSelections(quiz : qobj.Quiz, canv : tk.Canvas,
                        selected_v : tk.StringVar, selected_e : tk.StringVar,
                         sol_txt : tk.StringVar, sol_btn_txt : tk.StringVar, marks_txt : tk.StringVar):
    
    quiz.questions[quiz.current_question].graph.selected_edges = []
    quiz.questions[quiz.current_question].graph.selected_vertices = []

    quiz.questions[quiz.current_question].solution_toggled = False
    sol_txt.set('')
    sol_btn_txt.set('Show solution')
    marks_txt.set('')
    quiz.questions[quiz.current_question].graph.defaultGraph(canv)

    selected_v.set(value = 'Selected Vertices:\n[' + ' , '.join(qgui.verticesToLabelText(quiz.questions[quiz.current_question].graph.selected_vertices)) + ']' )

    selected_e.set(value = 'Selected Edges:\n[' + ' , '.join(qgui.edgesToLabelText(quiz.questions[quiz.current_question].graph.selected_edges)) + ']')

def toggleSolution(quiz : qobj.Quiz, solution_text : tk.StringVar, awarded_marks : tk.StringVar, btn_txt : tk.StringVar, canv : tk.Canvas):

    quiz.questions[quiz.current_question].markQuestion()

    hidden_str = ''

    if primsQuestion(quiz.questions[quiz.current_question]):
        shown_solution = 'Solution:\n[' + ' , '.join(qgui.edgesToLabelText(quiz.questions[quiz.current_question].solution)) + ']'
    
    elif kruskalsQuestion(quiz.questions[quiz.current_question]):
        shown_solution = 'Solution:\n[' + ' , '.join(qgui.edgesToLabelText(quiz.questions[quiz.current_question].solution)) + ']'
    
    shown_marks = "Awarded " + str(quiz.questions[quiz.current_question].markQuestion()) + " out of " + str(quiz.questions[quiz.current_question].marks) + " marks"

    quiz.questions[quiz.current_question].solution_toggled = not(quiz.questions[quiz.current_question].solution_toggled)
    toggle = quiz.questions[quiz.current_question].solution_toggled
 
    if toggle:
        #display solution
        solution_text.set(shown_solution)
        awarded_marks.set(shown_marks)
        btn_txt.set('Hide solution')

        if primsQuestion(quiz.questions[quiz.current_question]):
            quiz.questions[quiz.current_question].graph.markEdges(canv, quiz.questions[quiz.current_question].solution)

        elif kruskalsQuestion(quiz.questions[quiz.current_question]):
            quiz.questions[quiz.current_question].graph.markEdges(canv, quiz.questions[quiz.current_question].solution)


    else:
        #hide solution
        solution_text.set(hidden_str)
        awarded_marks.set(hidden_str)
        btn_txt.set('Show solution')
        quiz.questions[quiz.current_question].graph.colourEdges(canv)
        quiz.questions[quiz.current_question].graph.colourEdges(canv)

def showNextStep(quiz : qobj.Quiz, canv : tk.Canvas):
    #if the user's current solution is correct so far, show the next correct step
    #if not, tell the user the current solution is wrong

    #takes the length of the user's current solution
    current_step = len(quiz.questions[quiz.current_question].graph.selected_edges)
    users_current_solution = quiz.questions[quiz.current_question].graph.selected_edges

    #if the user already has the correct solution
    if users_current_solution == quiz.questions[quiz.current_question].solution:
        quiz.questions[quiz.current_question].graph.markEdges(canv, users_current_solution)

    #if the users solution is correct so far,
    elif users_current_solution == quiz.questions[quiz.current_question].solution[0:(current_step)]:
        next_edge = quiz.questions[quiz.current_question].solution[current_step]
        edge_id = quiz.questions[quiz.current_question].graph.getIdFromObj(next_edge, quiz.questions[quiz.current_question].graph.e_map)
        canv.itemconfig(edge_id, fill = 'orange')

    #tell user solution is wrong
    else:
        user_current_edge = users_current_solution[current_step - 1]
        edge_id = quiz.questions[quiz.current_question].graph.getIdFromObj(user_current_edge, quiz.questions[quiz.current_question].graph.e_map)
        canv.itemconfig(edge_id, fill = 'red')
        



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
    gui_elements = qgui.initGraphGui(app,CANV_W, CANV_H, quiz)

    canv = gui_elements[0]
    right_frame = gui_elements[1]
    canv_frame = gui_elements[2]

    #random generation (for testing)
    #v_list = ggen.generateRandomVertices(CANV_W,CANV_H, 24)
    #e_list = ggen.generateRandomEdges(v_list, 1, 20)

    #current question
    current_question = quiz.current_question
    quiz.questions[quiz.current_question].solution_toggled = False

    #create graph obj
    graph = quiz.questions[current_question].graph

    qgui.drawGraph(app,graph,canv,quiz,right_frame, canv_frame)

def nextQuestion(app : ttk.Window, quiz : qobj.Quiz, next_text : tk.StringVar):
    #there is a slight delay between clearing the screen and drawing new objects, causing flicker
    #this could be made less noticeable by updating only the text and graph as opposed to all of
    #the frames and buttons, but this is not a priority.

    #if not on last question, increment to go to next question
    if quiz.current_question != quiz.num_questions:
        quiz.current_question += 1

        #clears the window, then redraws the screen with the new current question
        af.clearWindow(app)

        if quiz.current_question == quiz.num_questions:
            next_text.set(value = 'End quiz')

        getSelectedGobj(quiz)
        drawQuizScreen(app, quiz)

        

    #if on last question
    else:
        #raise Exception('Reached end of questions.')
        st.gotoMarkingMenu(app, quiz)
    

def prevQuestion(app : ttk.Window, quiz : qobj.Quiz):
    #there is a slight delay between clearing the screen and drawing new objects, causing flicker
    #this could be made less noticeable by updating only the text and graph as opposed to all of
    #the frames and buttons, but this is not a priority.

    #if not on first question, increment to go to next question
    if quiz.current_question != 1:
        quiz.current_question -= 1

        #clears the window, then redraws the screen with the new current question
        af.clearWindow(app)
        getSelectedGobj(quiz)
        drawQuizScreen(app, quiz)
    
    #nothing happens if on first question - button will do nothing.
    
    
    

    
