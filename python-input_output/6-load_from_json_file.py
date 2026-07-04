#!/usr/bin/python3
"""Module for loading a Python object from a JSON file."""

import json


def load_from_json_file(filename):
    """Return the Python object stored inside a JSON file."""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
