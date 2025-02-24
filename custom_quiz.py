import quiz_objects as qobj
import custom_graph as cg
import random as r

def generatePrimsQuestion():
    return qobj.PrimsQuestion(graph = cg.getRandomGraph1(), marks = 5)


def generateQuiz1(num_questions : int):
    questions = {}

    for i in range(1, num_questions + 1):
        questions[i] = generatePrimsQuestion()

    return qobj.Quiz(
        questions
    )