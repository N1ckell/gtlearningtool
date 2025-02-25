import tkinter as tk
import ttkbootstrap as ttk
import graph_objects as gobj
import quiz_objects as qobj
import graph_generation as ggen
import quiz_nav as qnav

GUI_PADDING = 30
LABEL_PADDING = 20
INNER_PADDING = 5
FONT_SIZE = 'Calibri 20'

CANV_COLOUR = 'white'
CANV_PADDING = 50

def createCanvas(app : ttk.Window,
                 canv_w : int, canv_h : int,
                 canv_colour : str):
    #create canvas
    canv = tk.Canvas(app, width = canv_w, height = canv_h)
    canv.config(background= canv_colour)
    canv.pack(padx = INNER_PADDING, pady = INNER_PADDING, side = 'left', fill = 'both')

    return canv

def verticesToLabelText(vertex_list : list[gobj.Vertex]):
    return [vertex.label for vertex in vertex_list]

def edgesToLabelText(edge_list : list[gobj.Edge]):
    label_text = []
    
    for edge in edge_list:

        text = edge.v1.label + edge.v2.label
        label_text.append(text)
    return label_text

def createGuiFrame(app: ttk.Window):

    gui_frame = tk.Frame(master = app)
    gui_frame.pack(side = 'right', expand= True, fill = 'both',
                   padx = INNER_PADDING, pady = INNER_PADDING)
    return gui_frame

def initGraphGui(app : ttk.Window, CANV_W: int, CANV_H : int):

    main_frame = tk.Frame(master = app)
    main_frame.config(bg = app.cget('background'))
    main_frame.pack(side = 'bottom', fill = 'both', expand = True)
    #create canvas
    canv = createCanvas(main_frame, CANV_W, CANV_H, CANV_COLOUR)

    #create side gui
    gui_frame = createGuiFrame(main_frame)

    #return so canvas can be worked with
    return [canv, gui_frame]

def createSelectionGui(app : ttk.Window, graph : gobj.Graph, right_frame : ttk.Frame, canv : tk.Canvas):
    #creates the selected edge / vertex display
    #and returns the text variables to be updated when necessary

    selv_str = tk.StringVar(value = 'Selected Vertices:\n[' + ' , '.join(verticesToLabelText(graph.selected_vertices)) + ']' )

    selectedv_label = ttk.Label(master = right_frame, textvariable = selv_str, font = FONT_SIZE)
    selectedv_label.pack(padx = LABEL_PADDING, pady=LABEL_PADDING, anchor='w')

    
    sele_str = tk.StringVar(value = 'Selected Edges:\n[' + ' , '.join(edgesToLabelText(graph.selected_edges)) + ']')

    selectede_label = ttk.Label(master = right_frame, textvariable = sele_str, font = FONT_SIZE)
    selectede_label.pack(padx = LABEL_PADDING, pady=LABEL_PADDING, anchor='w')

    return [selv_str, sele_str]

def drawQuizNumber(app : ttk.Window, frame : ttk.Frame, quiz : qobj.Quiz):
    question_num_txt = tk.StringVar(value = 'Question ' + str(quiz.current_question) + ' of ' + str(quiz.num_questions))
    question_number = tk.Label(master = frame, textvariable = question_num_txt, font = FONT_SIZE)
    question_number.config(bg = app.cget('bg'))
    question_number.pack(side = 'right',anchor='se',padx = INNER_PADDING, pady = INNER_PADDING)

def drawQuizMarks(frame : ttk.Frame, quiz : qobj.Quiz):
    marks_txt = tk.StringVar(
        value = "[" + str(quiz.questions[quiz.current_question].marks) + " Marks]"
        )
    
    mark_txt_label = tk.Label(master = frame, textvariable = marks_txt,font = FONT_SIZE)
    mark_txt_label.pack(padx = LABEL_PADDING, pady=LABEL_PADDING, anchor='se', side='top')

def drawQuizQuestion(frame : ttk.Frame, quiz : qobj.Quiz):
    question_txt = tk.StringVar(
        value = (quiz.questions[quiz.current_question].question)
        )
    
    question_txt_lbl = tk.Label(master = frame, textvariable = question_txt,font = FONT_SIZE, anchor = 'w', justify = 'left')

    question_txt_lbl.bind('<Configure>', lambda e: question_txt_lbl.config(wraplength= frame.winfo_width() - GUI_PADDING))
    question_txt_lbl.pack(padx = LABEL_PADDING, pady=LABEL_PADDING, anchor='w', side='top', fill = 'both')

def getSolutionTxt(frame : ttk.Frame, quiz : qobj.Quiz):
    solution_txt = tk.StringVar(
        value = ''
        )
    return solution_txt
    
def drawSolutionLabel(frame : ttk.Frame, quiz : qobj.Quiz, solution_txt : tk.StringVar):

    solution_label = tk.Label(master = frame, textvariable = solution_txt ,font = FONT_SIZE)

    solution_label.pack(padx = LABEL_PADDING, pady=LABEL_PADDING, side='bottom', anchor='w')

    return solution_label




def drawQuestionNavBtn(app : ttk.Window, quiz : qobj.Quiz, frame : ttk.Frame):
    nextq_btn = ttk.Button(master = frame, text=">", command = lambda : qnav.nextQuestion(app, quiz), takefocus=False)
    nextq_btn.pack(side='right', padx = LABEL_PADDING, pady = LABEL_PADDING)
    lastq_btn = ttk.Button(master = frame, text="<", command = lambda : qnav.prevQuestion(app, quiz), takefocus=False)
    lastq_btn.pack(side='right', padx = LABEL_PADDING, pady = LABEL_PADDING)



def drawMarkBtn(frame : ttk.Frame, quiz : qobj.Quiz, solution_text : tk.Label, canv : tk.Canvas):
    btn_text = tk.StringVar(value = 'Show solution')
    mark_btn = ttk.Button(master = frame, textvariable = btn_text, command= lambda : qnav.toggleSolution(quiz, solution_text, btn_text, canv), takefocus=False)
    mark_btn.pack(side='left', padx = LABEL_PADDING, pady = LABEL_PADDING)

def createGraphGui(app : ttk.Window, graph : gobj.Graph, right_frame : ttk.Frame, canv : tk.Canvas, quiz : qobj.Quiz):

    #################
    #QUIZ RELATED ELEMENTS
    #################

    top_ui_frame = tk.Frame(master = app)
    top_ui_frame.config(bg = app.cget('bg'))
    top_ui_frame.pack(fill = 'x')

    #back button
    back_btn = ttk.Button(master = top_ui_frame, text="Back to main menu", takefocus=False)
    back_btn.pack(side='left', anchor='w', padx = INNER_PADDING, pady = INNER_PADDING)

    #quiz number
    drawQuizNumber(app, top_ui_frame, quiz)
    
    #quiz question
    drawQuizQuestion(right_frame, quiz)
    
    #quiz marks
    drawQuizMarks(right_frame, quiz)
    

    #################
    #CREATE SELECTION DISPLAY
    #################

    sel_label_var = createSelectionGui(app,graph,right_frame,canv)

    #################
    #CREATE BUTTONS
    #################
    
    #btn = ttk.Button(master = right_frame, text="Start Prim's Algorithm", command = lambda : graph.primsAlgorithm(canv))
    #btn.pack()

    #right frame bottom buttons
    nav_button_frame = tk.Frame(master = right_frame)
    nav_button_frame.pack(side='bottom', fill = 'x')

    solution_txt = getSolutionTxt(right_frame, quiz)

    solution_label = drawSolutionLabel(right_frame, quiz, solution_txt)

    drawMarkBtn(nav_button_frame, quiz, solution_txt, canv)
    
    drawQuestionNavBtn(app, quiz, nav_button_frame)
    

    return sel_label_var

def drawGraph(app : ttk.Window, graph : gobj.Graph, canv : tk.Canvas, quiz : qobj.Quiz, parent_frame : tk.Frame):
    #draw and get mapping
    graph.e_map = ggen.drawEdges(canv, graph.edges)
    graph.v_map = ggen.drawVertices(canv, graph.vertices)

    #create gui labels
    ggui_labels = createGraphGui(app, graph, parent_frame, canv, quiz)

    #bind canvas objects to corresponding click functions
    ggen.bindShapetoObj(canv, graph, ggui_labels)
