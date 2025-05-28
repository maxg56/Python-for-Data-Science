import math


def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing:", object, type(object))
        return 0
    elif isinstance(object, float) and math.isnan(object):
        print("Cheese:", object, type(object))
        return 0
    elif object == 0 and isinstance(object, int):
        print("Zero:", object, type(object))
        return 0
    elif object == "" and isinstance(object, str):
        print("Empty:", type(object))
        return 0
    elif object is False:
        print("Fake:", object, type(object))
        return 0
    else:
        print("Type not found")
        return 1
