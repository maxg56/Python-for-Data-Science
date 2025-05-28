def callLimit(limit: int):
    if not isinstance(limit, int):
        raise ValueError("limit must be an int")

    def decorate(func):
        """ Decorator to limit the number of calls to a function."""
        count = 0

        def inner(*args, **kargs):
            """ Execute the function and count the number of calls."""
            nonlocal count
            count += 1
            if (count > limit):
                print(f'Error: {func} call too many times')
                return
            return func(*args, **kargs)
        return inner
    return decorate
