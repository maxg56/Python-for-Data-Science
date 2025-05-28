import sys
import string


def count_character_types(text: str):
    """
    Count the number of different character types in the given text.
    Args:
        text (str): The text to analyze.
    """
    upper = sum(1 for c in text if c.isupper())
    lower = sum(1 for c in text if c.islower())
    punct = sum(1 for c in text if c in string.punctuation)
    space = sum(1 for c in text if c.isspace())
    digit = sum(1 for c in text if c.isdigit())

    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punct} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")


def main():
    """
    main function to handle input and call the character counting function.
    If no arguments are provided, it prompts the user for input.
    If an argument is provided, it uses that as the text to analyze.
    Raises:
        AssertionError: If more than one argument is provided.
    Raises:
        EOFError: If no input is provided when prompted.
    Raises:
        ValueError: If the input is not a valid string
        (not applicable here, but good practice).
    """
    if len(sys.argv) == 1:
        try:
            text = input("What is the text to analyse?\n")
        except EOFError:
            return
    else:
        assert len(sys.argv) == 2, " \
            AssertionError: more than one argument is provided"
        text = sys.argv[1]

    count_character_types(text)


if __name__ == "__main__":
    main()
