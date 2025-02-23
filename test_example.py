import tkinter as tk
import ttkbootstrap as ttk
import graph_generation as ggen
import graph_gui as ggui
import graph_objects as gobj
import custom_graph as cg
import quiz_objects as qobj
import custom_quiz as cq
import quiz_nav as qnav


WINDOW_BG = 'lightgrey'

#create app window
app = ttk.Window(title= 'GT Learning Tool')
app.config(background = WINDOW_BG)
#starts the window maximised
app.state('zoomed')

qnav.drawQuizScreen(app)

app.mainloop()