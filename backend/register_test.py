from database import create_database, add_user
from face_service import get_face_encoding


def register_user():

    print("login user")
    create_database()
    image_path = "test.jpg"

    print("wait for Face Encoding...")

    try:

        face_encoding = get_face_encoding(image_path)

        if face_encoding is None:

            print("cant find face")
            return

        print("Face Encoding crate.")

        print("count :", len(face_encoding))

        full_name = "qasem Test"

        cart_number = "222-22-22-22"

        cvv2 = "789"

        password = "123"
        add_user(
            full_name,
            cart_number,
            cvv2,
            password,
            face_encoding
        )

        print("login successfull")

    except Exception as e:

        print("eror:")
        print(e)


if __name__ == "__main__":

    register_user()