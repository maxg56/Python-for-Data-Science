import sys
from ft_filter import ft_filter


def main():
    """
    Main function to filter words based on their length.
    It expects two command line arguments:
    1. A string of words separated by spaces.
    2. An integer that specifies the minimum length of words to keep.
    If the arguments are not provided correctly, it raises an AssertionError.
    If the second argument is not an integer, it raises a ValueError.
    """
    if len(sys.argv) != 3:
        print("AssertionError: the arguments are bad")
        return

    try:
        number = int(sys.argv[2])
    except ValueError:
        print("AssertionError: argument is not an integer")
        return

    string = sys.argv[1]
    words = string.split(" ")
    filtered = ft_filter(lambda x: len(x) >= number, words)
    print(list(filtered))


if __name__ == "__main__":
    main()
