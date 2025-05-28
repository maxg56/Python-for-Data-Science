import sys

MORSE_CODE_DICT = {
    'A': '.-',    'B': '-...',  'C': '-.-.',
    'D': '-..',   'E': '.',     'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',
    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',
    'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ' ': '/'
}


def text_to_nested_morse(text: str) -> str:
    """
    Encode du texte en Morse, retourne une chaîne Morse avec espaces
      entre lettres et slash entre mots.
    Args:
        text (str): Le texte à encoder.
    Returns:
        str: Le texte encodé en Morse.
    Raises:
        ValueError: Si le texte contient des caractères non valides.
    """
    text = text.upper()
    if not all(char in MORSE_CODE_DICT for char in text):
        raise ValueError("AssertionError: the arguments are bad")
    return " / ".join(
        " ".join(MORSE_CODE_DICT[char] for char in word)
        for word in text.split()
    )


def main():
    """
    Main function to handle input and call the Morse code conversion function.
    It expects one command line argument:
    1. A string to convert to Morse code.
    If the argument is not provided or is invalid, it raises an AssertionError.
    Raises:
        AssertionError: If the number of arguments is not exactly one.
        ValueError: If the input text contains invalid characters.
    """
    if len(sys.argv) != 2:
        print("AssertionError: the arguments are bad")
        return
    text = sys.argv[1]
    try:
        morse_code = text_to_nested_morse(text)
        print(morse_code)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
