import sqlite3
import os
import json


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

            cart_number TEXT  NOT NULL,

            cvv2 TEXT NOT NULL,

            password TEXT NOT NULL,

            face_encoding TEXT NOT NULL

        )
    """)

    connection.commit()

    connection.close()

    print("Database created successfully.")


def add_user(
    full_name,
    cart_number,
    cvv2,
    password,
    face_encoding
):

    connection = get_connection()

    cursor = connection.cursor()

    face_encoding_json = json.dumps(face_encoding)

    cursor.execute("""
        INSERT INTO users
        (
            full_name,
            cart_number,
            cvv2,
            password,
            face_encoding
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        full_name,
        cart_number,
        cvv2,
        password,
        face_encoding_json
    ))

    connection.commit()

    connection.close()

    print("User added successfully.")


def get_user_by_cart_number(cart_number):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM users
        WHERE cart_number = ?
    """, (cart_number,))

    user = cursor.fetchone()

    connection.close()

    return user


if __name__ == "__main__":

    create_database()

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM users
    """)

    users = cursor.fetchall()

    connection.close()

    print()

    print("Users count:", len(users))

    for user in users:

        print()

        print("ID:", user["id"])
        print("Full Name:", user["full_name"])
        print("Cart Number:", user["cart_number"])