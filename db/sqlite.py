import sqlite3 as sq


async def db_start():
    with sq.connect("db/store.db") as db:

        db = sq.connect("db/store.db")
        cur = db.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS phones(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name TEXT, 
        price INTEGER, 
        characteristics TEXT, 
        photo TEXT
        )""")
        db.commit()


async def insert_product(category, name, price, characteristics, photo):
    with sq.connect("db/store.db") as db:
        cur = db.cursor()
        cur.execute(f"""
        INSERT INTO {category}(name, price, characteristics, photo) 
        VALUES('{name}', {price}, '{characteristics}', '{photo}')
        """)


async def select_product():
    with sq.connect("db/store.db") as db:
        cur = db.cursor()
        cur.execute(f"""
        SELECT * FROM phones WHERE name == "Apple Iphone"
        """)
        return cur.fetchall()