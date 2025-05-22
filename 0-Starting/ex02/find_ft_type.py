def all_thing_is_obj(object: any) -> int:
    if isinstance(object, list):
        print("List :", type(object))
    elif isinstance(object, tuple):
        print("Tuple :", type(object))
    elif isinstance(object, set):
        print("Set :", type(object))
    elif isinstance(object, dict):
        print("Dict :", type(object))
    elif isinstance(object, str):
        if object == "Brian is in the kitchen":
            print("Brian is in the kitchen :", type(object))
        else:
            print("Toto is in the kitchen :", type(object))
    else:
        print("Type not found")
    return 42



# if '__main__' == __name__:
#     all_thing_is_obj(42)
#     all_thing_is_obj("42")
#     all_thing_is_obj([1, 2, 3])
#     all_thing_is_obj((1, 2, 3))
#     all_thing_is_obj({1: "one", 2: "two"})
#     all_thing_is_obj({1, 2, 3})