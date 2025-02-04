class QuizQuestion():
    def __init__(self, question : str, solution : str, marks : int = 1):
        self.question = question
        self.solution = solution
        self.marks = marks

class Quiz():
    def __init__(self, quiz_type : str,
                 questions : dict[str , str],
                 marking_type :str = 'None'):
        
        self.quiz_type = quiz_type
        self.questions = questions
        self.num_questions = len(questions)
        self.marking_type = marking_type