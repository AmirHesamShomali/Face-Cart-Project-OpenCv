import sqlite3
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, "database.db")


def get_connection():

    connection = sqlite3.connect(DATABASE_PATH)

    connection.row_factory = sqlite3.Row

    return connection


def create_database():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            full_name TEXT NOT NULL,

            cart_number TEXT UNIQUE NOT NULL,

            cvv2 TEXT NOT NULL,

            password TEXT NOT NULL,

            face_encoding TEXT NOT NULL

        )
    """)

    connection.commit()

    connection.close()

    print("Database created successfully.")


def show_users():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users")

    users = cursor.fetchall()

    print("Users:")

    for user in users:
        print(dict(user))

    connection.close()


if __name__ == "__main__":

    create_database()

    show_users()