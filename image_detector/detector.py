import cv2
import numpy as np


def check_image_in_image(large_image_path, small_image_path, threshold=0.8):
    """
    Vérifie si une petite image est présente dans une grande image.

    :param large_image_path: Chemin vers la grande image.
    :param small_image_path: Chemin vers la petite image.
    :param threshold: Seuil de correspondance (entre 0 et 1).
    :return: True si la petite image est trouvée dans la grande image, sinon False.
    """

    large_image = cv2.imread(large_image_path)
    small_image = cv2.imread(small_image_path)

    if large_image is None:
        print(f"Failed to read image: {large_image_path}")
        return False
    if small_image is None:
        print(f"Failed to read image: {small_image_path}")
        return False

    large_image_gray = cv2.cvtColor(large_image, cv2.COLOR_BGR2GRAY)
    small_image_gray = cv2.cvtColor(small_image, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(large_image_gray, small_image_gray, cv2.TM_CCOEFF_NORMED)

    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))

    if locations:
        for loc in locations:
            print(f"location: {loc}")
        return True
    else:
        return False
