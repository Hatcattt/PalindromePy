"""
Author : https://github.com/Hatcattt

PalindromePy

This program can check if a sentence (or a word) is a palindrome
or not with a function called is_palindrome(sentence).

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
        ".": ""}


def normalize(sentence):
    """
    Return a new sentence in lowercase letters
    changing all accented letters to normal letters,
    remove spaces and punctuation marks.
    :return: string
    """
    for char in sentence.lower():
        if char in LETTERS_TO_CHANGE.keys():
            sentence = sentence.lower().replace(char, LETTERS_TO_CHANGE[char])
    return sentence


def is_palindrome(sentence):
    """
    Return True if the string in parameter
    is a palindrome, False otherwise
    :return: boolean
    """
    sentence = normalize(sentence)
    return (sentence == sentence[::-1]) if len(sentence) > 2 else False


# Exemples:
print("\nIs it a palindrome?\n")

sentences_to_test = [
    "stats",
    "3568653",
    "I'am a palindrome!",
    "I did, did I?",
    "Élu par cette crapule !"]

for example in sentences_to_test:
    print(is_palindrome(example), ':', example)
