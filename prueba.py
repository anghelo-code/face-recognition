from deepface import DeepFace
from typing import Tuple
import cv2
import numpy as np

def face_matching_sface_model() -> Tuple[bool, float]:
  try:
    # Redimensionar las imágenes al mismo tamaño
    # target_size = (230, 230)  # Tamaño objetivo, por ejemplo, 224x224 píxeles
    # face_1 = cv2.resize(face_1, target_size)
    # face_2 = cv2.resize(face_2, target_size)

    # print(face_1.shape)
    # print(face_2.shape)


    result = DeepFace.verify(img1_path="face_1_resized.jpg", img2_path="face_2_resized.jpg", model_name="SFace")
    matching, distance = result['verified'], result['distance']
    print("gaaaaaaaa")

    return matching, distance
  

  except Exception as e:
    print(f"An error occurred: {e}")
    return False, 0.0

print(face_matching_sface_model())


