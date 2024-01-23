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

def addUser(username, password):
    cursor.execute(f"""
    insert into user(username, password) VALUES ('{username}', '{password}')
    """)
    conObj.commit()
