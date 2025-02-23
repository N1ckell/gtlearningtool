import graph_objects as gobj

class Question():
    def __init__(self, graph : gobj.Graph, question : str, marks : int = 1):
        self.question = question
        self.marks = marks
        self.graph = graph

class PrimsQuestion(Question):
    def __init__(self, graph : gobj.Graph, question : str, solution : list[gobj.Edge], marks = 1):
        super().__init__(graph, question, marks)

        self.solution = solution

class Quiz():
    def __init__(self,
                 questions : dict[int , Question]
                 ):
        
        self.current_question = 1
        self.questions = questions
        self.num_questions = len(questions)