import numpy as np
from typing import Union, List

def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
        Return an array of each BMI for each couple of height:weight
    """
    if type(height) != list or type(weight) != list:
        raise ValueError('Height and weight must be lists')

    height = np.asarray(height)
    weight = np.asarray(weight)

    if (
        height.dtype not in ['float64', 'int32'] or
        weight.dtype not in ['float64', 'int32']
    ):
        raise ValueError('Height and weight must only contains int or float')
    if height.shape != weight.shape:
        raise ValueError('Height and weight must have the same size')

    squared_height = np.multiply(height, height)

    return np.divide(weight, squared_height).tolist()



def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
        Return an array of boolean that indicate if the element at the
        same index is above the limit.
    """
    return [x > limit for x in bmi]


if __name__ == "__main__":
    # Example usage
    heights = [1.75, 1.80, 1.65]
    weights = [70, 80, 60]
    try:
        bmis = give_bmi(heights, weights)
        print("BMIs:", bmis)
        print("Above limit 25:", apply_limit(bmis, 25))
    except Exception as e:
        print("Error:", e)
