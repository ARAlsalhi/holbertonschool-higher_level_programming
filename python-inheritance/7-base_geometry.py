#!/usr/bin/python3
"""Module that defines a BaseGeometry class with integer validation."""


class BaseGeometry:
    """Class that defines a base geometry object with validation."""

    def area(self):
        """Raises an Exception since area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer."""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
