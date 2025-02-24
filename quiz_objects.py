import graph_objects as gobj
import random as r

class Question():
    def __init__(self, graph : gobj.Graph, question : str, marks : int = 1):
        self.question = question
        self.marks = marks
        self.graph = graph
        self.solution = 'NULL'

class PrimsQuestion(Question):
    def __init__(self, graph : gobj.Graph, marks = 1):
        
        super().__init__(graph, marks)

        self.starting_vertex = self.graph.vertices[r.randint(0,len(self.graph.vertices) - 1)]

        self.question = "Select the correct order of edges to create an MST for this graph using Prim's algorithm. Start from vertex " + self.starting_vertex.label + "."

        self.solution = graph.primsAlgorithm(self.starting_vertex)

        self.marks = marks


        

class Quiz():
    def __init__(self,
                 questions : dict[int , Question]
                 ):
        
        self.current_question = 1
        self.questions = questions
        self.num_questions = len(questions)