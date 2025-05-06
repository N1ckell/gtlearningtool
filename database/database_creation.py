import sqlite3

sqlite_connection = sqlite3.connect('database/graphs.db')
cursor = sqlite_connection.cursor()

#creates a table for the graphs if it
#doesn't already exist

graph_table = '''
    CREATE TABLE IF NOT EXISTS graphs(
    id INTEGER PRIMARY KEY
    )
'''

cursor.execute(graph_table)

#creates a table for the vertices if it
#doesn't already exist

vertices_table = '''
    CREATE TABLE IF NOT EXISTS vertices(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    xpos INTEGER NOT NULL,
    ypos INTEGER NOT NULL,
    label TEXT NOT NULL,
    graph_id INTEGER NOT NULL,
    FOREIGN KEY (graph_id) REFERENCES graphs(id)
    )
'''
cursor.execute(vertices_table)

#creates a table for the edges if it
#doesn't already exist

edges_table = '''
    CREATE TABLE IF NOT EXISTS edges(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    v1_id INTEGER NOT NULL,
    v2_id INTEGER NOT NULL,
    graph_id INTEGER NOT NULL,
    FOREIGN KEY (v1_id) REFERENCES vertices(id),
    FOREIGN KEY (v2_id) REFERENCES vertices(id),
    FOREIGN KEY (graph_id) REFERENCES graphs(id)
    )
'''

cursor.execute(edges_table)


#close connection
sqlite_connection.close()
