from ft_calculator import calculator
try:

    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5
    print("---")
    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5
    print("---")
    v3 = calculator([10.0, 15.0, 20.0])
    v3 - 5
    v3 / 5
    print("---")
    try:
        v4 = calculator(90)
    except TypeError as e:
        print("Error:", e)
    try:
        v5 = calculator([1.0, 2.0, 3.0])
        v5 + "a"
    except TypeError as e:
        print("Error:", e)
    try:
        v6 = calculator([1.0, 2.0, 3.0])
        v6 / 0
    except ZeroDivisionError as e:
        print("Error:", e)
    try:
        v7 = calculator([1.0, 2.0, 3.0])
        v7 * "a"
    except TypeError as e:
        print("Error:", e)
except Exception as e:
    print("Error:", e)
