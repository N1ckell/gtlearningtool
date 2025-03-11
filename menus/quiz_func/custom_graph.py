import menus.quiz_func.graph_objects as gobj
import random as r

MAX_WEIGHT = 200

def getRandomGraph1():

    vertices = [gobj.Vertex([50,50],'a'),
                gobj.Vertex([50,300],'b'),
                gobj.Vertex([200,450],'c'),
                gobj.Vertex([600,100],'d'),
                gobj.Vertex([450,600],'e'),
                gobj.Vertex([400,300],'f'),
                gobj.Vertex([500,25],'g'),
                gobj.Vertex([200,50],'h'),
            ]

    edges = [gobj.Edge(vertices[0], vertices[1], label = r.randint(1,MAX_WEIGHT)),
            gobj.Edge(vertices[0], vertices[2], label = r.randint(1,MAX_WEIGHT)),
            gobj.Edge(vertices[2], vertices[4], label = r.randint(1,MAX_WEIGHT)),
            gobj.Edge(vertices[4], vertices[3], label = r.randint(1,MAX_WEIGHT)),
            gobj.Edge(vertices[0], vertices[7], label = r.randint(1,MAX_WEIGHT)),
            gobj.Edge(vertices[3], vertices[6], label = r.randint(1,MAX_WEIGHT)),
            gobj.Edge(vertices[5], vertices[2], label = r.randint(1,MAX_WEIGHT)),

            gobj.Edge(vertices[3], vertices[7], label = r.randint(1,MAX_WEIGHT)),
            gobj.Edge(vertices[4], vertices[7], label = r.randint(1,MAX_WEIGHT)),
            gobj.Edge(vertices[5], vertices[7], label = r.randint(1,MAX_WEIGHT))
    ]

    return gobj.Graph(vertices,edges)

def getRandomGraph2():

    vertices = [gobj.Vertex([100,300],'a'),
                gobj.Vertex([500,300],'b'),
                gobj.Vertex([450,100],'c'),
                gobj.Vertex([200,50],'d'),
                gobj.Vertex([150,450],'e'),
                gobj.Vertex([450,600],'f'),
            ]

    edges = [gobj.Edge(vertices[0], vertices[2], label = r.randint(1,MAX_WEIGHT)),
            gobj.Edge(vertices[1], vertices[4], label = r.randint(1,MAX_WEIGHT)),
            gobj.Edge(vertices[2], vertices[3], label = r.randint(1,MAX_WEIGHT)),
            gobj.Edge(vertices[0], vertices[4], label = r.randint(1,MAX_WEIGHT)),
            gobj.Edge(vertices[4], vertices[2], label = r.randint(1,MAX_WEIGHT)),
            gobj.Edge(vertices[1], vertices[5], label = r.randint(1,MAX_WEIGHT)),
            gobj.Edge(vertices[1], vertices[2], label = r.randint(1,MAX_WEIGHT)),
            gobj.Edge(vertices[4], vertices[5], label = r.randint(1,MAX_WEIGHT)),
    ]

    return gobj.Graph(vertices,edges)

def getRandomGraph3():

    vertices = [gobj.Vertex([100,100],'a'),
                gobj.Vertex([650,650],'b'),
                gobj.Vertex([450,700],'c'),
                gobj.Vertex([750,200],'d'),
                gobj.Vertex([250,150],'e'),
                gobj.Vertex([700,450],'f'),
                gobj.Vertex([600,50],'g'),
                gobj.Vertex([350,600],'h'),
                gobj.Vertex([150,450],'i'),
                gobj.Vertex([50,600],'j'),
            ]

    edges = [gobj.Edge(vertices[0], vertices[2], label = r.randint(1,MAX_WEIGHT)),
            gobj.Edge(vertices[1], vertices[4], label = r.randint(1,MAX_WEIGHT)),
            gobj.Edge(vertices[0], vertices[4], label = r.randint(1,MAX_WEIGHT)),
            gobj.Edge(vertices[1], vertices[2], label = r.randint(1,MAX_WEIGHT)),
            gobj.Edge(vertices[4], vertices[5], label = r.randint(1,MAX_WEIGHT)),
            gobj.Edge(vertices[3], vertices[7], label = r.randint(1,MAX_WEIGHT)),
            gobj.Edge(vertices[4], vertices[6], label = r.randint(1,MAX_WEIGHT)),
            gobj.Edge(vertices[0], vertices[8], label = r.randint(1,MAX_WEIGHT)),
            gobj.Edge(vertices[0], vertices[9], label = r.randint(1,MAX_WEIGHT)),
            gobj.Edge(vertices[7], vertices[9], label = r.randint(1,MAX_WEIGHT)),
            gobj.Edge(vertices[8], vertices[9], label = r.randint(1,MAX_WEIGHT)),
            gobj.Edge(vertices[3], vertices[6], label = r.randint(1,MAX_WEIGHT)),
            gobj.Edge(vertices[3], vertices[5], label = r.randint(1,MAX_WEIGHT)),
            gobj.Edge(vertices[1], vertices[5], label = r.randint(1,MAX_WEIGHT)),
    ]

    return gobj.Graph(vertices,edges)

def getRandomGraph4():

    vertices = [gobj.Vertex([600,450],'a'),
                gobj.Vertex([400,50],'b'),
                gobj.Vertex([100,450],'c'),
                gobj.Vertex([650,250],'d'),
                gobj.Vertex([200,150],'e'),
                gobj.Vertex([550,650],'f'),
                gobj.Vertex([350,700],'g'),
                gobj.Vertex([150,650],'h'),
            ]

    edges = [gobj.Edge(vertices[0], vertices[1], label = r.randint(1,MAX_WEIGHT)),
            gobj.Edge(vertices[1], vertices[2], label = r.randint(1,MAX_WEIGHT)),
            gobj.Edge(vertices[2], vertices[3], label = r.randint(1,MAX_WEIGHT)),
            gobj.Edge(vertices[3], vertices[4], label = r.randint(1,MAX_WEIGHT)),
            gobj.Edge(vertices[4], vertices[5], label = r.randint(1,MAX_WEIGHT)),
            gobj.Edge(vertices[5], vertices[6], label = r.randint(1,MAX_WEIGHT)),
            gobj.Edge(vertices[7], vertices[6], label = r.randint(1,MAX_WEIGHT)),
            gobj.Edge(vertices[2], vertices[5], label = r.randint(1,MAX_WEIGHT)),
            gobj.Edge(vertices[2], vertices[7], label = r.randint(1,MAX_WEIGHT)),

            gobj.Edge(vertices[4], vertices[1], label = r.randint(1,MAX_WEIGHT)),
            gobj.Edge(vertices[1], vertices[3], label = r.randint(1,MAX_WEIGHT)),
            gobj.Edge(vertices[3], vertices[0], label = r.randint(1,MAX_WEIGHT)),
        
        
    ]

    return gobj.Graph(vertices,edges)

def getRandomGraph5():

    vertices = [gobj.Vertex([100,450],'a'),
                gobj.Vertex([500,150],'b'),
                gobj.Vertex([400,600],'c'),
                gobj.Vertex([150,200],'d'),
                gobj.Vertex([600,250],'e'),
            ]

    edges = [gobj.Edge(vertices[0], vertices[1], label = r.randint(1,MAX_WEIGHT)), 
             gobj.Edge(vertices[1], vertices[2], label = r.randint(1,MAX_WEIGHT)), 
             gobj.Edge(vertices[2], vertices[3], label = r.randint(1,MAX_WEIGHT)), 
             gobj.Edge(vertices[3], vertices[4], label = r.randint(1,MAX_WEIGHT)), 
             gobj.Edge(vertices[0], vertices[2], label = r.randint(1,MAX_WEIGHT)), 
             gobj.Edge(vertices[2], vertices[4], label = r.randint(1,MAX_WEIGHT)), 
    ]

    return gobj.Graph(vertices,edges)

    
#g = getRandomGraph1()
#g.kruskalsAlgorithm()

