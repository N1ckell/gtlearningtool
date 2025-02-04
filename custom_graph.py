import graph_objects as gobj
import random as r

vertices = [gobj.Vertex([50,50],'a'),
            gobj.Vertex([50,300],'b'),
            gobj.Vertex([200,450],'c'),
            gobj.Vertex([600,100],'d'),
            gobj.Vertex([450,600],'e'),
            gobj.Vertex([500,300],'f'),
            gobj.Vertex([500,25],'g'),
            gobj.Vertex([200,50],'h'),
        ]

edges = [gobj.Edge(vertices[0], vertices[1], label = r.randint(1,5)),
         gobj.Edge(vertices[0], vertices[2], label = r.randint(1,5)),
         gobj.Edge(vertices[2], vertices[4], label = r.randint(1,5)),
         gobj.Edge(vertices[4], vertices[3], label = r.randint(1,5)),
         gobj.Edge(vertices[0], vertices[7], label = r.randint(1,5)),
         gobj.Edge(vertices[3], vertices[6], label = r.randint(1,5)),
         gobj.Edge(vertices[5], vertices[2], label = r.randint(1,5)),
]

graph = gobj.Graph(vertices,edges)