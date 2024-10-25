import sqlite3


def initiate_db(db_name='database1.db'):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        ) 
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL
        ) 
    ''')

    connection.commit()
    connection.close()
    return initiate_db


# db = initiate_db()
#
#
# def create_bd(db_name='database1.db'):
#     connection = sqlite3.connect(db_name)
#     cursor = connection.cursor()
#
#     for i in range(1, 5):
#         cursor.execute('INSERT INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)',
#                        (f'{i}', f'Продукт {i}', f'Описание {i}', f'{100 * i}'))
#
#     connection.commit()
#     connection.close()
#     return create_bd
#
#
# cr = create_bd()


def get_all_products(db_name='database1.db'):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    back = cursor.fetchall()
    connection.close()
    return back


def add_user(username, email, age):
    connection = sqlite3.connect('database1.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', (username, email, age, 1000))
    connection.commit()


def is_included(username):
    connection = sqlite3.connect('database1.db')
    cursor = connection.cursor()
    check_user = cursor.execute('SELECT * FROM Users WHERE username=?', (username, ))
    if check_user.fetchone() is None:
        return False
    else:
        return True
