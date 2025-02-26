import tkinter as tk
import ttkbootstrap as ttk
import string
import menus.quiz_func.graph_objects as gobj
import random as r
import menus.quiz_func.quiz_gui as qgui

CANVAS_COLOUR = 'white'

#=====================================================================#
#GRAPH SPECIFIC FUNCTIONS
#=====================================================================#

def createGraph(vertices : list[gobj.Vertex], edges : list[gobj.Edge]):
    return gobj.Graph(vertices,edges)

#=====================================================================#
#DRAW TO CANVAS FUNCTIONS
#=====================================================================#

def drawEdges(canv : tk.Canvas, edge_list : list[gobj.Edge]):
    #draws edges from edge_list, then
    #maps edges drawn to the canvas (using unique id) to their
    #corresponding variable of type gobj.Edge, then returns
    #edge_map

    edge_map : dict[int , gobj.Edge] = {}

    for edge in edge_list:

        #if edge isn't selected
        if edge.state == False:
            drawn_edge = canv.create_line(
                edge.pos1[0],edge.pos1[1],
                edge.pos2[0],edge.pos2[1],
                width = edge.width,
                fill = edge.colour,
                activewidth = edge.active_width,
                tags = 'edge'
            )
        
        #if edge is selected
        else:
            drawn_edge = canv.create_line(
                edge.pos1[0],edge.pos1[1],
                edge.pos2[0],edge.pos2[1],
                width = edge.active_width,
                fill = edge.active_colour,
                activewidth = edge.active_width,
                tags = 'edge'
            )


        edge_map[drawn_edge] = edge

        label = canv.create_text(
            edge.line_center[0], edge.line_center[1],
            text = edge.label,
            fill = edge.label_colour,
            font = 'Arial '+ edge.label_size,
            state = 'disabled')

        label_bbox = canv.bbox(label)
        
        label_outline = canv.create_oval(label_bbox, fill= CANVAS_COLOUR,
                                            outline = CANVAS_COLOUR,
                                            state = 'disabled')

        canv.tag_raise(label,label_outline)

    return edge_map

def drawVertices(canv : tk.Canvas, vertex_list : list[gobj.Vertex]):
    #draws vertices from vertex_list, then
    #maps vertices drawn to the canvas (using unique id) to their
    #corresponding variable of type gobj.Vertex, then returns
    #vertex_map

    vertex_map : dict[int , gobj.Vertex] = {}

    for vertex in vertex_list:

        #if vertex not selected
        if vertex.state == False:
            drawn_vertex = canv.create_oval(
                vertex.tk_circle_points[0],
                vertex.tk_circle_points[1],
                vertex.tk_circle_points[2],
                vertex.tk_circle_points[3],
                fill = vertex.fill,
                activefill = vertex.active_fill,
                outline = vertex.outline,
                activeoutline = vertex.active_outline,
                width = vertex.width,
                activewidth = vertex.active_width,
                tags = 'vertex'
            )

        else:
                drawn_vertex = canv.create_oval(
                vertex.tk_circle_points[0],
                vertex.tk_circle_points[1],
                vertex.tk_circle_points[2],
                vertex.tk_circle_points[3],
                fill = vertex.active_fill,
                activefill = vertex.active_fill,
                outline = vertex.active_outline,
                activeoutline = vertex.active_outline,
                width = vertex.active_width,
                activewidth = vertex.active_width,
                tags = 'vertex'
            )

        #maps each vertex object to it's drawn counterpart
        #on the canvas into a dict
        vertex_map[drawn_vertex] = vertex

        #draw vertex label
        canv.create_text(
            vertex.center[0], vertex.center[1],
            text = vertex.label,
            fill = vertex.label_colour,
            font = 'Arial '+ vertex.label_size,
            state = 'disabled')
        
    return vertex_map

#=====================================================================#
#ON CLICK FUNCTIONS
#=====================================================================#

def clickedVertex(e, canv : tk.Canvas, graph : gobj.Graph, vertex_label : tk.StringVar):

    #returns all items currently under the mouse (using 'current')
    #and returns them as a tuple, hence the indexing
    clicked_vertex = (canv.find_withtag('current'))[0]

    vertex = graph.v_map[clicked_vertex]

    if vertex.state == False:
        vertex.state = True

        canv.itemconfig(clicked_vertex, fill=vertex.active_fill)
        canv.itemconfig(clicked_vertex, width=vertex.active_width)
        canv.itemconfig(clicked_vertex, outline=vertex.active_outline)

        #used to keep track of the order in which vertices are selected
        graph.selected_vertices.append(vertex)


    else:
        vertex.state = False
        canv.itemconfig(clicked_vertex, fill=vertex.fill)
        canv.itemconfig(clicked_vertex, width=vertex.width)
        canv.itemconfig(clicked_vertex, outline=vertex.outline)

        #used to keep track of the order in which vertices are selected
        graph.selected_vertices.remove(vertex)

    vertex_label.set('Selected Vertices:\n[' + ' , '.join(qgui.verticesToLabelText(graph.selected_vertices)) + ']' )
    
    


    #selected_label.set('Selected Vertices: ' + ','.join(ggui.getSelectedVertices(vertex_map)))


def clickedEdge(e, canv : tk.Canvas, graph : gobj.Graph,  edge_label : tk.StringVar):
    #returns all items currently under the mouse (using 'current')
    #and returns them as a tuple, hence the indexing
    clicked_edge = (canv.find_withtag('current'))[0]

    edge = graph.e_map[clicked_edge]

    if edge.state == False:
        edge.state = True
        canv.itemconfig(clicked_edge, width=edge.active_width)
        canv.itemconfig(clicked_edge, fill=edge.active_colour)

        #used to keep track of the order in which edges are selected
        graph.selected_edges.append(edge)

    else:
        edge.state = False
        canv.itemconfig(clicked_edge, width=edge.width)
        canv.itemconfig(clicked_edge, fill=edge.colour)

        #used to keep track of the order in which edges are selected
        graph.selected_edges.remove(edge)

    edge_label.set('Selected Edges:\n[' + ' , '.join(qgui.edgesToLabelText(graph.selected_edges)) + ']')


#=====================================================================#
#BIND FUNCTIONS
#=====================================================================#

def bindShapetoObj(canv : tk.Canvas, 
                  graph : gobj.Graph,
                  ggui_labels : list[tk.StringVar]):
    
    #binds shapes on the given canvas with the tag 'vertex' to the
    #function clickedVertex when left clicked
    canv.tag_bind('vertex','<Button-1>', lambda e : clickedVertex(e, canv, graph, ggui_labels[0]))

    #binds shapes on the given canvas with the tag 'edge' to the
    #function clickedEdge when left clicked
    canv.tag_bind('edge','<Button-1>', lambda e : clickedEdge(e, canv, graph, ggui_labels[1]))

    

#=====================================================================#
#TEST FUNCTIONS (randomly generates vertices / edges to test display)
#=====================================================================#

def generateRandomVertices(canv_width : int,canv_height : int, num_vertices = r.randint(0,25)):
    #generate vertices
    #used only in testing to view different
    #randomly generated layouts of edges / vertices
    #between 0 and 25 as the labels are from ascii_uppercase

    if num_vertices > 25:
        raise Exception('Number of requested vertices exceeds the maximum.')

    generated_vertices : list[gobj.Vertex] = []
    vertex_labels = list(string.ascii_uppercase)

    for i in range(1,num_vertices):
        generated_vertices.append(
            gobj.Vertex([r.randint(0 + (2 *gobj.CIRCLE_RADIUS),
                                   canv_width - (2 *gobj.CIRCLE_RADIUS)),
                         r.randint(0 + (2 *gobj.CIRCLE_RADIUS),
                                   canv_height - (2 *gobj.CIRCLE_RADIUS))],
                        label = vertex_labels.pop())
        )
    
    return generated_vertices

def generateRandomEdges(vertex_list : list[gobj.Vertex], min_weight : int, max_weight : int):
    #generate edges between vertices
    #in given list
    connected_vertices : list[gobj.Edge] = []

    for i in range(1,12):
        pair = [vertex_list[r.randint(0,len(vertex_list)-1)],
                    vertex_list[r.randint(0,len(vertex_list)-1)]
                    ]
        

        #uses reversed as connecting vertex A to B
        #is the same as attaching B to A
        while pair in connected_vertices or reversed(pair) in connected_vertices:
            pair = [vertex_list[r.randint(0,len(vertex_list)-1)],
                    vertex_list[r.randint(0,len(vertex_list)-1)]
                    ]
            
        
        connected_vertices.append(
            gobj.Edge(
                pair[0],
                pair[1],
                label = str(r.randint(min_weight,max_weight))
            )
        )
    
    return connected_vertices