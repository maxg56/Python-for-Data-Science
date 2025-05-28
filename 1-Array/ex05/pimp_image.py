import numpy as np


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Inverts the colors of the image.
    """
    return 255 - array


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Keeps only the red channel.
    """
    red_channel = array[:, :, 0]
    return np.stack([
        red_channel,
        np.zeros_like(red_channel),
        np.zeros_like(red_channel)
    ], axis=2).astype(np.uint8)


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Keeps only the green channel.
    """
    green_channel = array[:, :, 1]
    return np.stack([
        np.zeros_like(green_channel),
        green_channel,
        np.zeros_like(green_channel)
    ], axis=2).astype(np.uint8)


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Keeps only the blue channel.
    """
    blue_channel = array[:, :, 2]
    return np.stack([
        np.zeros_like(blue_channel),
        np.zeros_like(blue_channel),
        blue_channel
    ], axis=2).astype(np.uint8)


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Converts the image to grayscale by averaging the RGB channels.
    """
    image = np.mean(array, axis=2, keepdims=True).astype(array.dtype)
    return np.repeat(image, 3, axis=2)
