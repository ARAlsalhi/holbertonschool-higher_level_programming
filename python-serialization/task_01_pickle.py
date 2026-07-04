#!/usr/bin/env python3
"""Module for serializing and deserializing custom objects with pickle."""

import pickle


class CustomObject:
    """Represent a custom object that can be pickled."""

    def __init__(self, name, age, is_student):
        """Initialize a CustomObject instance."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize the current object and save it to a file."""
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except (OSError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load and return a CustomObject instance from a pickle file."""
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)

            if isinstance(obj, cls):
                return obj

            return None
        except (OSError, pickle.PickleError, EOFError):
            return None
