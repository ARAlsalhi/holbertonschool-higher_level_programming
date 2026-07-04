#!/usr/bin/python3
"""Module for converting an object to a dictionary."""


def class_to_json(obj):
    """Return the dictionary description of an object's attributes."""
    return obj.__dict__
