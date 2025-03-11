import sqlite3

sqlite_connection = sqlite3.connect('database/graphs.db')
cursor = sqlite_connection.cursor()

def insertG5():
    #graph 5 vertices
    #graphid, xpos, ypos, label
    g5vertices = [
        (5,100,450,'a'),
        (5,500,150,'b'),
        (5,400,600,'c'),
        (5,150,200,'d'),
        (5,600,250,'e')
    ]
    #graph5 edges
    g5edges = [
            (5,1,2),
            (5,3,4),
            (5,4,5),
            (5,1,3),
            (5,3,5)
    ]
    cursor.execute('''
        INSERT INTO graphs(id) VALUES(5)
    ''')
    cursor.executemany('''
        INSERT INTO vertices(graph_id, xpos, ypos, label) 
                VALUES (?, ?, ?, ?)''', g5vertices
    )
    cursor.executemany('''
        INSERT INTO edges(graph_id, v1_id, v2_id) 
                VALUES(?,?,?)''', g5edges
    )

insertG5()
  
sqlite_connection.commit()

sqlite_connection.close()
