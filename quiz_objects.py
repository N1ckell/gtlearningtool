import graph_objects as gobj

class Question():
    def __init__(self, question : str, graph : gobj.Graph, marks : int = 1):
        self.question = question
        self.marks = marks
        self.graph = graph

class PrimsQuestion(Question):
    def __init__(self, solution : list[gobj.Edge], question, graph, marks = 1):
        super().__init__(question, graph, marks)

        self.solution = solution

class Quiz():
    def __init__(self,
                 questions : dict[int , Question],
                 marking_type : str = 'None'):
        
        self.questions = questions
        self.num_questions = len(questions)
        self.marking_type = marking_type