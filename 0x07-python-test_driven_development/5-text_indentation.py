#!/usr/bin/python3


def text_indentation(text):
    """Print text with indentation"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for k in range(len(text)):
        if text[k] in [".", "?", ":"]:
            print("")
            print("")
        else:
            print(text[k], end="")
