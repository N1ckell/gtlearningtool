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

def insertG1():

    g1vertices = [
        (1,50,50,'a'),
        (1,50,300,'b'),
        (1,200,450,'c'),
        (1,600,100,'d'),
        (1,450,600,'e'),
        (1,400,300,'f'),
        (1,500,25,'g'),
        (1,200,50,'h')
    ]


    g1edges = [
            (1,1,2),
            (1,3,5),
            (1,5,4),
            (1,1,8),
            (1,4,7),
            (1,6,3),
            (1,4,8),
            (1,5,8),
            (1,6,8)
    ]

    cursor.execute('''
        INSERT INTO graphs(id) VALUES(1)
    ''')
    cursor.executemany('''
        INSERT INTO vertices(graph_id, xpos, ypos, label) 
                VALUES (?, ?, ?, ?)''', g1vertices
    )
    cursor.executemany('''
        INSERT INTO edges(graph_id, v1_id, v2_id) 
                VALUES(?,?,?)''', g1edges
    )
  
def insertG2():

    g2vertices = [
        (2,100,300,'a'),
        (2,500,300,'b'),
        (2,450,100,'c'),
        (2,200,50,'d'),
        (2,150,450,'e'),
        (2,450,600,'f')
    ]
    

    g2edges = [
            (2,1,3),
            (2,2,5),
            (2,3,4),
            (2,1,5),
            (2,5,3),
            (2,2,6),
            (2,2,3),
            (2,5,6)
    ]

    cursor.execute('''
        INSERT INTO graphs(id) VALUES(2)
    ''')
    cursor.executemany('''
        INSERT INTO vertices(graph_id, xpos, ypos, label) 
                VALUES (?, ?, ?, ?)''', g2vertices
    )
    cursor.executemany('''
        INSERT INTO edges(graph_id, v1_id, v2_id) 
                VALUES(?,?,?)''', g2edges
    )

def insertG3():

    g3vertices = [
        (3,100,100,'a'),
        (3,650,650,'b'),
        (3,450,700,'c'),
        (3,750,200,'d'),
        (3,250,150,'e'),
        (3,700,450,'f'),
        (3,600,50,'g'),
        (3,350,600,'h'),
        (3,150,450,'i'),
        (3,50,600,'j')
            ]

    g3edges = [
            (3,1,3),
            (3,2,5),
            (3,1,5),
            (3,2,3),
            (3,5,6),

            (3,4,8),
            (3,5,7),
            (3,1,9),
            (3,1,10),
            (3,8,10),

            (3,9,10),
            (3,4,7),
            (3,4,6),
            (3,2,6)
    ]

    cursor.execute('''
        INSERT INTO graphs(id) VALUES(3)
    ''')
    cursor.executemany('''
        INSERT INTO vertices(graph_id, xpos, ypos, label) 
                VALUES (?, ?, ?, ?)''', g3vertices
    )
    cursor.executemany('''
        INSERT INTO edges(graph_id, v1_id, v2_id) 
                VALUES(?,?,?)''', g3edges
    )

def insertG4():

    g4vertices = [
        (4,600,450,'a'),
        (4,400,50,'b'),
        (4,100,450,'c'),
        (4,650,250,'d'),
        (4,200,150,'e'),
        (4,550,650,'f'),
        (4,350,700,'g'),
        (4,150,650,'h')
            ]
    
    g4edges = [
            (4,1,2),
            (4,2,3),
            (4,3,4),
            (4,4,5),
            (4,5,6),

            (4,6,7),
            (4,8,7),
            (4,3,6),
            (4,3,8),
            (4,5,2),

            (4,2,4),
            (4,4,1)
            
    ]

    cursor.execute('''
        INSERT INTO graphs(id) VALUES(4)
    ''')
    cursor.executemany('''
        INSERT INTO vertices(graph_id, xpos, ypos, label) 
                VALUES (?, ?, ?, ?)''', g4vertices
    )
    cursor.executemany('''
        INSERT INTO edges(graph_id, v1_id, v2_id) 
                VALUES(?,?,?)''', g4edges
    )

'''
insertG1()
insertG2()
insertG3()
insertG4()
insertG5()
'''


sqlite_connection.commit()

sqlite_connection.close()
