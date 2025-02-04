import tkinter as tk
import ttkbootstrap as ttk
import graph_objects as gobj

GUI_PADDING = 50
LABEL_PADDING = 5
FONT_SIZE = 'Calibri 30'

def verticesToLabelText(vertex_list : list[gobj.Vertex]):
    return [vertex.label for vertex in vertex_list]

def edgesToLabelText(edge_list : list[gobj.Edge]):
    label_text = []
    
    for edge in edge_list:

        text = edge.v1.label + edge.v2.label
        label_text.append(text)

    return label_text

def createGuiFrame(app: ttk.Window):

    gui_frame = ttk.Frame(master = app)
    gui_frame.pack(side = 'right', expand= True, fill = 'both',
                   padx = GUI_PADDING, pady = GUI_PADDING)
    return gui_frame

def createGraphGui(app : ttk.Window, graph : gobj.Graph, main_frame : ttk.Frame):
    selv_str = tk.StringVar(value = 'Selected Vertices: ' + ' , '.join(graph.selected_vertices))

    selectedv_label = ttk.Label(master = main_frame, textvariable = selv_str, font = FONT_SIZE)
    selectedv_label.pack(padx = LABEL_PADDING, pady=LABEL_PADDING)

    #print(selectedv_label.cget('textvariable'))

    sele_str = tk.StringVar(value = 'Selected Edges: ' + ' , '.join(graph.selected_vertices))

    selectede_label = ttk.Label(master = main_frame, textvariable = sele_str, font = FONT_SIZE)
    selectede_label.pack(padx = LABEL_PADDING, pady=LABEL_PADDING)

    #print(selectede_label.cget('textvariable'))

    return [selv_str, sele_str]