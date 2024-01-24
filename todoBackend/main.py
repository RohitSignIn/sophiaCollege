import mysql.connector

config = {
    "port": 7777,
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "tododb"
}

conObj = mysql.connector.connect(**config)

cursor = conObj.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS user(
        id int auto_increment primary key,
        username text,
        password text
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS todo(
        id int auto_increment primary key,
        task text,
        status text,
        userId int,
        foreign key(userId) references user(id)
    )
""")


# USER Query
def addUser(username, password):
    cursor.execute(f"""
    insert into user(username, password) VALUES ('{username}', '{password}')
    """)
    conObj.commit()

def getUser(userId):
    cursor.execute(f"""
    select * from user where id = '{userId}'
    """)
    res = cursor.fetchone()
    return res

def getUsers():
    cursor.execute(f"""
    select * from user
    """)
    res = cursor.fetchall()
    return res

def updateUser(update, to, userId):
    cursor.execute(f"""
    update user set {update} = '{to}' 
    where id = '{userId}'
    """)
    return

def removeUser(userId):
    cursor.execute(f"""
    delete from user 
    where id = '{userId}'
    """)
    return

# Todo Query
def addTodo(task, userId):
    cursor.execute(f"""
    insert into todo(task, status, userId) 
    VALUES ('{task}', 'pending', '{userId}')
    """)
    conObj.commit()

def getTodos():
    cursor.execute(f"""
    select * from todo
    """)
    res = cursor.fetchall()
    return res

def getTodo(todoId):
    cursor.execute(f"""
    select * from todo 
    where id = '{todoId}'
    """)
    res = cursor.fetchone()
    return res

def getUserTodo(userId):
    cursor.execute(f"""
    select * from todo 
    where userId = '{userId}'
    """)
    res = cursor.fetchall()
    return res


def updateTodo(update, to, todoId):
    cursor.execute(f"""
    update todo set {update} = '{to}' 
    where id = '{todoId}'
    """)
    return

def removeTodo(todoId):
    cursor.execute(f"""
    delete from todo 
    where id = '{todoId}'
    """)
    return