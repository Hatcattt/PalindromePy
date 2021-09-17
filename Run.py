# Letters and punctuation marks to be replaced
LETTERS_TO_CHANGE = {
        "à": "a",
        "ä": "a",
        "â": "a",
        "ç": "c",
        "é": "e",
        "è": "e",
        "ê": "e",
        "ë": "e",
        "ï": "i",
        "ô": "o",
        "ù": "u",
        "ü": "u",
        "û": "u",
        " ": "",
        "-": "",
        "_": "",
        ",": "",
        "'": "",
        "?": "",
        "!": "",
        ".": "",
    }


def normalize(sentence):
    """
    This function returns a new sentence in lowercase letters changing all accented letters to normal letters,
    remove spaces and punctuation marks.

    :param sentence: string to transform (type string)
    :return: new sentence (type string)
    """
    for key, value in LETTERS_TO_CHANGE.items():
        sentence = sentence.replace(key, value).lower()
    return sentence


def is_palindrome(sentence):
    """
    This function return True if the string in parameter is a palindrome, False otherwise

    :param sentence: string to test (type string)
    :return: True if phrase is a palindrome, False otherwise (type bool)
    """

    if sentence is None or len(sentence) <= 2:
        return False

    sentence = normalize(sentence)
    return sentence == sentence.lower()[::-1]


sentence1 = "I am a palindrome!"
sentence2 = "Élu par cette crapule!"
sentence3 = "No, it is open on one position."

print(f"{sentence1} ->", is_palindrome(sentence1))
print(f"{sentence2} ->", is_palindrome(sentence2))
print(f"{sentence3} ->", is_palindrome(sentence3))

# Output:

# I am a palindrome! -> False
# Élu par cette crapule! -> True
# No, it is open on one position. -> True
