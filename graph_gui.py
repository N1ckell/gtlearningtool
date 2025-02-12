import tkinter as tk
import ttkbootstrap as ttk
import graph_objects as gobj

GUI_PADDING = 50
LABEL_PADDING = 5
FONT_SIZE = 'Calibri 30'

def createCanvas(app : ttk.Window,
                 canv_w : int, canv_h : int,
                 canv_colour : str, padding : int):
    #create canvas
    canv = tk.Canvas(app, width = canv_w, height = canv_h)
    canv.config(background= canv_colour)
    canv.pack(padx = padding, pady= padding, side = 'left')

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
                   padx = GUI_PADDING, pady = GUI_PADDING)
    return gui_frame

def createGraphGui(app : ttk.Window, graph : gobj.Graph, main_frame : ttk.Frame, canv : tk.Canvas):
    selv_str = tk.StringVar(value = 'Selected Vertices: ' + ' , '.join(graph.selected_vertices))

    selectedv_label = ttk.Label(master = main_frame, textvariable = selv_str, font = FONT_SIZE)
    selectedv_label.pack(padx = LABEL_PADDING, pady=LABEL_PADDING)

    sele_str = tk.StringVar(value = 'Selected Edges: ' + ' , '.join(graph.selected_vertices))

    selectede_label = ttk.Label(master = main_frame, textvariable = sele_str, font = FONT_SIZE)
    selectede_label.pack(padx = LABEL_PADDING, pady=LABEL_PADDING)

    btn = ttk.Button(master = main_frame, text="Start Prim's Algorithm", command = lambda : graph.primsAlgorithm(canv))
    btn.pack()

    return [selv_str, sele_str]