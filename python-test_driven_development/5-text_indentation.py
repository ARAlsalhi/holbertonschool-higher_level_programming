#!/usr/bin/python3
"""This module provides a text indentation function."""


def text_indentation(text):
    """Print text with two new lines after '.', '?' and ':'."""
    if type(text) is not str:
        raise TypeError("text must be a string")

    new_line = True

    for char in text:
        if new_line and char == " ":
            continue

        print(char, end="")

        if char in ".?:":
            print("\n")
            new_line = True
        else:
            new_line = False
