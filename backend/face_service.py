from deepface import DeepFace


def get_face_encoding(image_path):

    result = DeepFace.represent(
        img_path=image_path,
        model_name="Facenet",
        detector_backend="opencv",
        enforce_detection=True
    )

    if not result:
        return None

    face_encoding = result[0]["embedding"]

    return face_encoding


if __name__ == "__main__":

    image_path = "face.jpg"

    try:

        encoding = get_face_encoding(image_path)

        if encoding is None:
            print("erors")
        else:
            print("Face encoding create")
            print(" count:", len(encoding))
            print("Encoding:")
            print(encoding)

    except Exception as e:

        print("eror")
        print(e)