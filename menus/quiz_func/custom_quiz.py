import menus.quiz_func.quiz_objects as qobj
import database.get_graph as get_graph
import random as r

TYPES_OF_GRAPH  = 5

def getRandomGraph():
    
    n = r.randint(1,TYPES_OF_GRAPH)

    return get_graph.getGraph(n)
        
def generatePrimsQuestion():
    return qobj.PrimsQuestion(graph = getRandomGraph(), marks = 5)

def generateKruskalsQuestion():
    return qobj.KruskalsQuestion(graph = getRandomGraph(), marks = 5)


def generateQuiz(num_questions : int, question_type : str):

    questions = {}

    for i in range (1, num_questions + 1):

        if question_type == 'Include All':
            random_question_type = r.randint(1,2)
        
        elif question_type == "Prim's Algorithm":
            random_question_type = 1
        
        elif question_type == "Kruskal's Algorithm":
            random_question_type = 2

        if random_question_type == 1:
            questions[i] = generatePrimsQuestion()
        
        elif random_question_type == 2:
            questions[i] = generateKruskalsQuestion()
        
        else:
            raise Exception('Random question number out of included range.')
    
    return qobj.Quiz(
    questions
    )