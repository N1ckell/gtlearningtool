import tkinter as tk
import ttkbootstrap as ttk
import graph_generation as ggen
import graph_gui as ggui
import custom_graph as cg

WINDOW_BG = 'lightgrey'
CANV_COLOUR = 'white'
CANV_PADDING = 50


#create app window
app = ttk.Window(title= 'GT Learning Tool')
app.config(background = WINDOW_BG)
#starts the window maximised
app.state('zoomed')
win_width = app.winfo_screenwidth()
win_height = app.winfo_screenheight()

CANV_W = int(win_width // 2.5)
CANV_H = int(win_height - (win_height // 4) )

#create canvas
canv = ggen.createCanvas(app, CANV_W, CANV_H, CANV_COLOUR, CANV_PADDING)

#create side gui
gui_frame = ggui.createGuiFrame(app)

#random generation (for testing)
v_list = ggen.generateRandomVertices(CANV_W,CANV_H, 24)
e_list = ggen.generateRandomEdges(v_list, 1, 20)

#create graph obj
graph = cg.graph
#ggen.createGraph(v_list, e_list)

#draw and get mapping
graph.e_map = ggen.drawEdges(canv, graph.edges)
graph.v_map = ggen.drawVertices(canv, graph.vertices)

#create gui labels
ggui_labels = ggui.createGraphGui(app, graph, gui_frame)

#bind canvas objects to corresponding click functions
ggen.bindShapetoObj(canv, graph, ggui_labels)

app.mainloop()