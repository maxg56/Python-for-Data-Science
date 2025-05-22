import sys
from ft_filter import ft_filter

def main():
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
