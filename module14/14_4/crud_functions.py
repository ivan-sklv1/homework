import sqlite3

def initiate_db():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    # cursor.execute('DELETE FROM Products')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        price INT NOT NULL
    );
    ''')
    # for i in range(1, 5):
    #     cursor.execute(
    #         'INSERT INTO Products (title, description, price) VALUES (?,?,?)', (
    #             (f'Продукт {i}', f'Описание {i}', i * 100)
    #         )
    #     )
    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT id, title, description, price FROM Products')
    db = cursor.fetchall()

    connection.commit()
    connection.close()
    return list(db)
