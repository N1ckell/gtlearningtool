import quiz_objects as qobj
import custom_graph as cg
import random as r

graph1 = cg.graph1
starting_vertex1 = graph1.vertices[r.randint(0,len(graph1.vertices) - 1)]
question1 = qobj.PrimsQuestion(graph = graph1,
                               question = "Select the correct order of edges to create an MST for this graph using Prim's algorithm. Start from vertex " + starting_vertex1.label + ".",
                               solution = graph1.primsAlgorithm(starting_vertex1),
                               marks = 5
                          )

graph2 = cg.graph2
starting_vertex2 = graph2.vertices[r.randint(0,len(graph2.vertices) - 1)]
question2 = qobj.PrimsQuestion(graph = graph2,
                               question = "Select the correct order of edges to create an MST for this graph using Prim's algorithm. Start from the vertex " + starting_vertex2.label + ".",
                               solution = graph2.primsAlgorithm(starting_vertex2),
                               marks = 6
                          )

custom_quiz = qobj.Quiz(
    {1:question1,2:question2}
)