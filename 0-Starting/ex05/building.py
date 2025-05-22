import sys
import string

def count_character_types(text: str):
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
    if len(sys.argv) == 1:
        try:
            text = input("What is the text to analyse?\n")
        except EOFError:
            return
    else:
        assert len(sys.argv) == 2, "AssertionError: more than one argument is provided"
        text = sys.argv[1]

    count_character_types(text)

if __name__ == "__main__":
    main()

