import sqlite3
import os
import json
import numpy as np

from face_service import get_face_encoding


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASE_PATH = os.path.join(BASE_DIR, "database.db")


def get_connection():

    connection = sqlite3.connect(DATABASE_PATH)

    connection.row_factory = sqlite3.Row

    return connection


def find_user_by_face(image_path):

    print("wait for Face Encoding...")

    face_encoding = get_face_encoding(image_path)

    if face_encoding is None:

        print("Face not found.")

        return None

    print("Face Encoding created.")

    print("count :", len(face_encoding))

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM users
    """)

    users = cursor.fetchall()

    connection.close()

    for user in users:

        saved_face_encoding = json.loads(
            user["face_encoding"]
        )

        face1 = np.array(face_encoding)

        face2 = np.array(saved_face_encoding)

        distance = np.linalg.norm(face1 - face2)

        print(
            "Checking:",
            user["full_name"]
        )

        print(
            "Distance:",
            distance
        )

        if distance < 0.6:

            return user

    return None


if __name__ == "__main__":

    print("Face Login")

    image_path = "face.jpg"

    user = find_user_by_face(image_path)

    if user:

        print()
        print("Login successful.")

        print("ID:", user["id"])
        print("Full Name:", user["full_name"])
        print("Cart Number:", user["cart_number"])
        print("cvv2 Number:", user["cvv2"])
        print("Password:", user["password"])


    else:

        print()
        print("User not found.")