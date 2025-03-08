import menus.quiz_func.graph_objects as gobj
import random as r

class Question():
    def __init__(self, graph : gobj.Graph, question : str, marks : int = 1):
        self.question = question
        self.marks = marks
        self.graph = graph
        self.solution = 'NULL'
        self.solution_toggled = False

class KruskalsQuestion(Question):
    def __init__(self, graph : gobj.Graph, marks = 1):
        
        super().__init__(graph, marks)

        self.question = "Select the correct order of vertices and edges to create an MST for this graph using Kruskal's algorithm."

        self.solution = graph.kruskalsAlgorithm()

        self.marks = len(self.solution)

    def markQuestion(self):
        awarded_marks = 0

        #for every edge which matches the order
        #of the solution, award a mark
        if len(self.graph.selected_vertices) > 0:
            for i in range (0,len(self.solution)):
                if not(i > len(self.graph.selected_vertices) - 1):
                    if self.graph.selected_vertices[i] == self.solution[i]:
                        awarded_marks += 1

            #take away a mark for every edge selected
            #over the number within the solution

        if len(self.solution) < len(self.graph.selected_vertices):
            awarded_marks -= (len(self.graph.selected_vertices) - len(self.solution))

        if awarded_marks < 0:
            awarded_marks = 0
            
        return awarded_marks

class PrimsQuestion(Question):
    def __init__(self, graph : gobj.Graph, marks = 1):
        
        super().__init__(graph, marks)

        self.starting_vertex = self.graph.vertices[r.randint(0,len(self.graph.vertices) - 1)]

        self.question = "Select the correct order of edges to create an MST for this graph using Prim's algorithm. Start from vertex " + self.starting_vertex.label + "."

        self.solution = graph.primsAlgorithm(self.starting_vertex)

        self.marks = len(self.solution)

    def markQuestion(self):
        awarded_marks = 0

        #for every edge which matches the order
        #of the solution, award a mark
        if len(self.graph.selected_edges) > 0:
            for i in range (0,len(self.solution)):
                if not(i > len(self.graph.selected_edges) - 1):
                    if self.graph.selected_edges[i] == self.solution[i]:
                        awarded_marks += 1

            #take away a mark for every edge selected
            #over the number within the solution

        if len(self.solution) < len(self.graph.selected_edges):
            awarded_marks -= (len(self.graph.selected_edges) - len(self.solution))

        if awarded_marks < 0:
            awarded_marks = 0
            
        return awarded_marks


        

class Quiz():
    def __init__(self,
                 questions : dict[int , Question]
                 ):
        
        self.current_question = 1
        self.questions = questions
        self.num_questions = len(questions)