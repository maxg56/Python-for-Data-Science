import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
        Slice an array using the given start and end.
        Display informations about the shape after before
        and after slicing.
    """
    if not isinstance(family, list):
        raise ValueError('Family must be a list')
    family_arr = np.asarray(family)
    print("My shape is : ", family_arr.shape)
    family_arr = family_arr[start:end]
    print("My new shape is", family_arr.shape)
    return family_arr
