#!/usr/bin/python3
"""Module that reads a UTF-8 text file."""


def read_file(filename=""):
    """Read a UTF-8 text file and print its contents to stdout."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
