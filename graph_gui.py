import tkinter as tk
import ttkbootstrap as ttk
import graph_objects as gobj
import quiz_objects as qobj

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

    selv_str = tk.StringVar(value = 'Selected Vertices:\n[]')

    selectedv_label = ttk.Label(master = right_frame, textvariable = selv_str, font = FONT_SIZE)
    selectedv_label.pack(padx = LABEL_PADDING, pady=LABEL_PADDING, anchor='w')

    sele_str = tk.StringVar(value = 'Selected Edges:\n[]')

    selectede_label = ttk.Label(master = right_frame, textvariable = sele_str, font = FONT_SIZE)
    selectede_label.pack(padx = LABEL_PADDING, pady=LABEL_PADDING, anchor='w')

    return [selv_str, sele_str]

def drawQuizNumber(app : ttk.Window, frame : ttk.Frame):
    question_num_txt = tk.StringVar(value = 'Question 1 of 10')
    question_number = tk.Label(master = frame, textvariable = question_num_txt, font = FONT_SIZE)
    question_number.config(bg = app.cget('bg'))
    question_number.pack(side = 'right',anchor='se',padx = INNER_PADDING, pady = INNER_PADDING)

def drawQuizMarks(frame : ttk.Frame):
    marks_txt = tk.StringVar(
        value = "[3 marks]"
        )
    
    mark_txt_label = tk.Label(master = frame, textvariable = marks_txt,font = FONT_SIZE)
    mark_txt_label.pack(padx = LABEL_PADDING, pady=LABEL_PADDING, anchor='se', side='top')

def drawQuizQuestion(frame : ttk.Frame):
    question_txt = tk.StringVar(
        value = "Create an MST for this graph using Prim's algorithm, given the starting vertex A."
        )
    
    question_txt_lbl = tk.Label(master = frame, textvariable = question_txt,font = FONT_SIZE, anchor = 'w', justify = 'left')

    question_txt_lbl.bind('<Configure>', lambda e: question_txt_lbl.config(wraplength= frame.winfo_width() - GUI_PADDING))
    question_txt_lbl.pack(padx = LABEL_PADDING, pady=LABEL_PADDING, anchor='w', side='top', fill = 'both')

def drawQuestionNavBtn(frame : ttk.Frame):
    nextq_btn = ttk.Button(master = frame, text=">")
    nextq_btn.pack(side='right', padx = LABEL_PADDING, pady = LABEL_PADDING)
    lastq_btn = ttk.Button(master = frame, text="<")
    lastq_btn.pack(side='right', padx = LABEL_PADDING, pady = LABEL_PADDING)

def drawMarkBtn(frame : ttk.Frame):
    mark_btn = ttk.Button(master = frame, text="Mark")
    mark_btn.pack(side='left', padx = LABEL_PADDING, pady = LABEL_PADDING)

def createGraphGui(app : ttk.Window, graph : gobj.Graph, right_frame : ttk.Frame, canv : tk.Canvas):

    #################
    #QUIZ RELATED ELEMENTS
    #################

    top_ui_frame = tk.Frame(master = app)
    top_ui_frame.config(bg = app.cget('bg'))
    top_ui_frame.pack(fill = 'x')

    #back button
    back_btn = ttk.Button(master = top_ui_frame, text="Back")
    back_btn.pack(side='left', anchor='w', padx = INNER_PADDING, pady = INNER_PADDING)

    #quiz number
    drawQuizNumber(app, top_ui_frame)
    
    #quiz question
    drawQuizQuestion(right_frame)
    
    #quiz marks
    drawQuizMarks(right_frame)
    

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

    drawMarkBtn(nav_button_frame)
    
    drawQuestionNavBtn(nav_button_frame)
    

    return sel_label_var
