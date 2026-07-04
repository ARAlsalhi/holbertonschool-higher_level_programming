#!/usr/bin/python3
"""Module that defines a Student class."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student instance."""
        if isinstance(attrs, list) and all(
                isinstance(attr, str) for attr in attrs):
            return {
                attr: getattr(self, attr)
                for attr in attrs
                if hasattr(self, attr)
            }

        return self.__dict__.copy()
