import sqlite3


def initiate_db(db_name='database.db'):
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

    connection.commit()
    connection.close()
    return initiate_db


db = initiate_db()


def create_bd(db_name='database.db'):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    for i in range(1, 5):
        cursor.execute('INSERT INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)',
                       (f'{i}', f'Продукт {i}', f'Описание {i}', f'{100 * i}'))

    connection.commit()
    connection.close()
    return create_bd


cr = create_bd()


def get_all_products(db_name='database.db'):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Products')
    back = cursor.fetchall()
    connection.close()
    return back
