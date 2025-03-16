import sqlite3
import menus.quiz_func.graph_objects as gobj
import random as r

MAX_EDGE_WEIGHT = 1000

def getGraph(graph_id : int):
    vertices = []
    vertices_to_edge = []
    edges = []

    sqlite_connection = sqlite3.connect('database/graphs.db')
    cursor = sqlite_connection.cursor()

    db_vertices = cursor.execute("SELECT * FROM vertices WHERE graph_id = " + str(graph_id))

    for row in db_vertices:
        vertex = gobj.Vertex([row[1],row[2]], row[3])
        vertices.append(vertex)
        vertices_to_edge.append(vertex)

    db_edges = cursor.execute("SELECT * FROM edges WHERE graph_id = " + str(graph_id))

    for row in db_edges:
        edges.append(gobj.Edge(
            vertices_to_edge[row[1] - 1],
            vertices_to_edge[row[2] - 1],
            label = r.randint(1,MAX_EDGE_WEIGHT)
            ))

    sqlite_connection.close()

    return gobj.Graph(vertices, edges)