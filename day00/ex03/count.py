import string as stri
import sys

def text_analyser(string = None, *bs) :
    """This function counts the number of upper characters, \
lower characters, ponctuation and spaces in a given text."""
    pass
    if len(bs) > 0 :
        print("ERROR")
        return
    if string is not None :
        print("The text contains", len(string), "characters:\n")
        print("-", sum(map(str.isupper, string)), "upper letters\n")
        print("-", sum(map(str.islower, string)), "lower letters\n")
        print("-", sum(map(isponctuation, string)), "punctuation marks\n")
        print("-", sum(map(str.isspace, string)), "spaces\n")
    else :
        get = input("What is the text to analyse ?\n")
        text_analyser(get)

def isponctuation(char) :
    return char in stri.punctuation