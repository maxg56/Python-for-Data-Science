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
    Converts the image to grayscale using the luminosity method:
    0.299 * R + 0.587 * G + 0.114 * B
    """
    grey = (
        0.299 * array[:, :, 0] +
        0.587 * array[:, :, 1] +
        0.114 * array[:, :, 2]
    ).astype(np.uint8)
    return grey 
