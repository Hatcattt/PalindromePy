"""
Author : https://github.com/Hatcattt

PalindromePy

This program check if a sentence (or a world) is a palindrome or not.
Return a boolean True if the sentence is a palindrome, False otherwise.

Work with french language too.

"""

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
    This function returns a new sentence in lowercase letters
    changing all accented letters to normal letters,
    remove spaces and punctuation marks.
    """
    for key, value in LETTERS_TO_CHANGE.items():
        sentence = sentence.replace(key, value).lower()
    return sentence


def is_palindrome(sentence):
    """
    This function return True if the string in parameter
    is a palindrome, False otherwise
    :return: True or False
    """
    sentence = normalize(sentence)
    return (sentence == sentence.lower()[::-1]) if len(sentence) > 2 else False

