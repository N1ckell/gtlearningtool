import math as m
import tkinter as tk

CIRCLE_RADIUS = 25
LABEL_SIZE = 15

class Vertex:
    def __init__(self, position = [0,0], label = 'NULL',
                  fill = 'purple4', outline = 'black',
                  active_fill = 'magenta1', active_outline = 'magenta4',
                  width = 2,
                  label_colour = 'white',
                  active_label_colour = 'black',
                  state = False):
        

        
        self.fill = fill
        self.active_fill = active_fill

        self.outline = outline
        self.active_outline = active_outline

        self.width = width
        self.active_width = width * 2


        self.label = label
        self.label_colour = label_colour
        self.label_size = str(LABEL_SIZE)
        self.active_label_colour = active_label_colour

        self.position = position
        #tk needs 4 coords for circle instead of 
        #2 and radius, but working w radius is easier (personally)
        self.tk_circle_points = self.getCirclePoints(
                                    self.position[0],
                                    self.position[1])
        
        self.center = self.getCircleCenter(
            self.tk_circle_points[0],
            self.tk_circle_points[1]
        )

        #is the vertex currently selected
        self.state = state
    
    def getCirclePoints(self, topLX, topLY):
        diameter = CIRCLE_RADIUS * 2
        return [topLX,topLY,topLX + diameter, topLY + diameter]

    def getCircleCenter(self, x1,y1):
        return [x1 + CIRCLE_RADIUS, y1 + CIRCLE_RADIUS]


class Edge:
    #takes the coords of two vertices to calc edge position
    def __init__(self, vertex1 : Vertex, vertex2 : Vertex,
                  canvas_colour = 'white',
                  label = '1', width = 3, colour = 'black',
                  active_colour = 'magenta',
                  label_colour = 'black', label_outline = 'white',
                  label_width = 3,
                  state = False):
        
        #used when wanting to display
        #what vertices this edge connects
        self.v1 = vertex1
        self.v2 = vertex2
    
        self.pos1 = [ vertex1.center[0],
                    vertex1.center[1] ]
        
        self.pos2 = [ vertex2.center[0],
                     vertex2.center[1] ]
        
        self.label = label
        self.label_size = str(LABEL_SIZE)
        self.label_colour = label_colour
        self.label_outline = canvas_colour
        self.label_width = label_width

        self.width = width
        self.active_width = width * 2

        self.colour = colour
        self.active_colour = active_colour

        self.line_center = self.getLineCenter()

        #is the edge currently selected
        self.state = state



    def getLineCenter(self):
        return [(self.pos1[0] + self.pos2[0]) / 2,
                (self.pos1[1] + self.pos2[1]) / 2]


class Graph:
    def __init__(self, vertices : list[Vertex], edges : list[Edge]):
        self.vertices = vertices
        self.edges = edges

        self.selected_vertices : list[Vertex] = []
        self.selected_edges : list[Edge] = []

        self.v_map : dict[int , Vertex] = {}
        self.e_map : dict[int , Edge] = {}

    def clearSelectedGobj(self):
        self.selected_edges = []
        self.selected_vertices = []

    def getAdjacentVertices(self, vertex : Vertex):
        #returns the adjacent vertices and the
        #edge connecting it to given vertex
        adjacent = []

        for edge in self.edges:
            if edge.v1 == vertex and (edge.v2, edge) not in adjacent:
                #x = (edge.v2.label, str(edge.v1.label) + str(edge.v2.label))
                x = (edge.v2, edge)
                adjacent.append(x)
            elif edge.v2 == vertex and (edge.v1, edge) not in adjacent:
                #y = (edge.v1.label, str(edge.v1.label) + str(edge.v2.label))
                y = (edge.v1, edge)
                adjacent.append(y)

        return adjacent
        
    def getIdFromObj(self, target_obj, target_dict : dict):
        #returns the canvas id of a shape
        #from v_map or e_map when given it's
        #corresponding edge or vertex

        id = list(filter(lambda obj: target_dict[obj] == target_obj, target_dict))

        return id
    
    def getLabel(self, edge : Edge):
        return int(edge.label)
    
    def defaultGraph(self, canv : tk.Canvas):

        for edge_id in self.e_map:
            for edge in self.edges:

                edge.state = False
                edge.width = 3
                edge.colour = 'black'
                edge.active_colour = 'magenta'
                edge.active_width = edge.width * 2

                canv.itemconfig(edge_id, fill = edge.colour)
                canv.itemconfig(edge_id, width = edge.width)
                canv.itemconfig(edge_id, activefill = edge.active_colour)
                canv.itemconfig(edge_id, activewidth = edge.active_width)

        for vertex_id in self.v_map:
            for vertex in self.vertices:

                vertex.state = False
                vertex.fill = 'purple4'
                vertex.outline = 'black'
                vertex.active_fill = 'magenta1'
                vertex.active_outline = 'magenta4'
                vertex.width = 2
                vertex.label_colour = 'white'

                canv.itemconfig(vertex_id, fill = vertex.fill)
                canv.itemconfig(vertex_id, width = vertex.width)
                canv.itemconfig(vertex_id, activefill = vertex.active_fill)
                canv.itemconfig(vertex_id, activewidth = vertex.active_width)
                canv.itemconfig(vertex_id, activeoutline = vertex.active_outline)
                canv.itemconfig(vertex_id, outline = vertex.outline)
                

    
    def colourEdges(self, canv : tk.Canvas):

        for edge_id in self.e_map:
            for edge in self.edges:

                if self.e_map[edge_id] == edge:

                    if edge.state == False:
                        canv.itemconfig(edge_id, fill = 'black')

                    else:
                        canv.itemconfig(edge_id, fill = 'magenta')


                    
    
    def colourVertices(self, canv : tk.Canvas):

        for vertex_id in self.v_map:
            for vertex in self.vertices:

                if self.v_map[vertex_id] == vertex:

                    if vertex.state == False:
                        canv.itemconfig(vertex_id, fill = 'purple4')
                        canv.itemconfig(vertex_id, outline = 'black')

                    else:
                        canv.itemconfig(vertex_id, fill = 'magenta1')
                        canv.itemconfig(vertex_id, outline = 'magenta4')
    
    def markEdges(self, canv : tk.Canvas, edge_list: list[Edge]):

        for edge_id in self.e_map:
            if self.e_map[edge_id].state == True:
                canv.itemconfig(edge_id, fill = 'red')

        #for all of the edge ids
        for edge_id in self.e_map:
            #and for all of the edges in the given prims solution
            for edge in edge_list:
                #(this if is just used so we have the id for the edge)

    
                if self.e_map[edge_id] == edge:

                    #if the user has selected the edge, make it green
                    if edge.state == True:
                        canv.itemconfig(edge_id, fill = 'green2')
                    
                    #if the user hasn't selected the edge, make it orange
                    else:
                        canv.itemconfig(edge_id, fill = 'orange')

    def markVertices(self, canv : tk.Canvas, vertex_list: list[Vertex]):

        for vertex_id in self.v_map:
            if self.v_map[vertex_id].state == True:
                canv.itemconfig(vertex_id, fill = 'red')

        #for all of the vertex ids
        for vertex_id in self.v_map:
            #and for all of the vertices in the given kruskals solution
            for vertex in vertex_list:
                #(this if is just used so we have the id for the vertex)

    
                if self.v_map[vertex_id] == vertex:

                    #if the user has selected the vertex, make it green
                    if vertex.state == True:
                        canv.itemconfig(vertex_id, fill = 'green2')
                    
                    #if the user hasn't selected the vertex, make it orange
                    else:
                        canv.itemconfig(vertex_id, fill = 'orange')


    def find(self, parent, vertex : Vertex):
        #if the parent of the given vertex isn't itself
        #(is child of another vertex), continue searching
        #up the tree
        if parent[vertex] != vertex:

            return self.find(parent,parent[vertex])
        
        #if this is the parent, return
        else:

            return parent[vertex]

    def union(self, parent, v1, v2):
        
        #find the parent of the given vertices
        v1parent = self.find(parent, v1)
        v2parent = self.find(parent, v2)

        #set parent of one group as the parent of the other group
        parent[v1parent] = v2parent



    def kruskalsAlgorithm(self):

        chosen_edges = []
        chosen_vertices = []

        #counts the number of edges taken
        #in the mst to know when to stop running
        #the algorithm
        edges_taken = 0

        #counts number of iterations, used to
        #index sorted_edges
        i = 0

        #init parent: dict{child : parent}
        parent = {}
        for vertex in self.vertices:
            #all vertices, by default, are their own parent
            #as each vertex is in it's own 'set'
            parent[vertex] = vertex

           
        #returns a list of the graphs edges in 
        #ascending weight order
        sorted_edges = sorted(self.edges, key = self.getLabel)

        while edges_taken < len(self.vertices) - 1:

            min_edge = sorted_edges[i]
            i += 1

            v1 = min_edge.v1
            v2 = min_edge.v2

            v1parent = self.find(parent, v1)
            v2parent = self.find(parent, v2)

            #if the parents of v1 and v2 arent the same
            #(won't cause a cycle), then include this
            #edge / vertices and continue
            if v1parent != v2parent:

                #append edge
                if min_edge not in chosen_edges:
                    chosen_edges.append(min_edge)
                    edges_taken += 1


                #append vertices
                if v1 not in chosen_vertices:
                    chosen_vertices.append(v1)
                if v2 not in chosen_vertices:
                    chosen_vertices.append(v2)

                #union the two sets of vertices
                self.union(parent, v1parent, v2parent)

        
        return chosen_edges
            
            

                        


    def primsAlgorithm(self, starting_vertex : Vertex):
        #init mst including starting vertex
        #starting_vertex = self.vertices(r.randint(0,len(self.vertices)))
        #starting_vertex = self.vertices[0]

        #canv.itemconfig(self.getIdFromObj(starting_vertex, self.v_map), fill = 'green2')
        mst = [starting_vertex]
        chosen_edges = []

        #loops until all vertices visited
        while len(mst) < len(self.vertices):

            #check the lowest weighted edge which connects a vertex
            #from the mst to a vertex outside the mst
            adjacent_vertices = []
            #current lowest edge weight
            min_weight = m.inf

            for vertex in mst:
                adjacent_vertices.append(self.getAdjacentVertices(vertex))
            
            for vertex_edge_list in adjacent_vertices:
                for pair in vertex_edge_list:
                    if pair[0] not in mst and pair[1].label < min_weight:

                        current_vertex = pair[0]
                        current_edge = pair[1]
                        min_weight = current_edge.label

            if current_vertex:
                mst.append(current_vertex)
                #canv.itemconfig(self.getIdFromObj(current_vertex, self.v_map), fill = 'green2')
                #current_vertex.state = True
                chosen_edges.append(current_edge)
                #current_edge.state = True
                #canv.itemconfig(self.getIdFromObj(current_edge, self.e_map), fill = 'green2')
        
        return chosen_edges




