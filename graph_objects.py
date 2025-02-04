import random as r
import math as m
import heapq as hq

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

        #value used in prims algorithm
        self.prims_value = m.inf
    
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