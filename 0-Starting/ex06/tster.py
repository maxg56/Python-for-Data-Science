from ft_filter import ft_filter


def test(items, func):
    """
    Print the result of the original filter and ft_filter
    for the given params

    Args:
        items (iterable)
        func (function)
    """
    it_filter = filter(func, items)
    it_ft_filter = ft_filter(func, items)
    print("---")
    print("   filter:", list(it_filter))
    print("ft_filter:", list(it_ft_filter))


def main():
    # Test is odd
    items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def is_odd(x):
        return x % 2 == 0
    test(items, is_odd)

    # Test with None
    items = [0, 1, False, True, "", "Not empty", {}, {'foo', 'bar'}]
    test(items, None)

    # Test with None and empty
    items = []
    test(items, None)

    # Test next
    items = [1, 2, 3]
    it_filter = filter(None, items)
    it_ft_filter = ft_filter(None, items)
    print("---")
    print("   next(filter):", next(it_filter))
    print("next(ft_filter):", next(it_ft_filter))
    print("   next(filter):", next(it_filter))
    print("next(ft_filter):", next(it_ft_filter))


if __name__ == "__main__":
    main()
