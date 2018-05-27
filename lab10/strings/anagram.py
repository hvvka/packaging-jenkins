import inspect
from collections import Counter


def is_anagram(word, _list):
    """
    Checks if the given word has its anagram(s)
    on the given list of words

    :param word: word
    :param _list: list of words
    :return a list of found anagrams
    """
    word = word.lower()
    anagrams = []
    for words in _list:
        if word != words.lower():
            if Counter(word) == Counter(words.lower()):
                anagrams.append(words)
    return anagrams


def get_code():
    """
    Returns the code for the is_anagram function

    :return source code
    """
    return inspect.getsource(is_anagram)
