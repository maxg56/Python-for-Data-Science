import sys


def main():
    if len(sys.argv) != 2:
        print("AssertionError: more than one argument is provided")
        return 0

    try:
        number = int(sys.argv[1])
    except ValueError:
        print("AssertionError: argument is not an integer")
        return 0

    if number % 2:
        print("I'm Odd.")
    else:
        print("I'm Even.")


if __name__ == "__main__":
    main()
