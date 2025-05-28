from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    """
    Load an image from the given path and return it as a numpy array.
    Args:
        path (str): The path to the image file.
    Returns:
        np.ndarray: The image represented as a numpy array.
    """
    try:
        img = Image.open(path)
        img_array = np.array(img)
        return img_array
    except Exception as e:
        raise ValueError(f"Could not load image: {e}") from e
