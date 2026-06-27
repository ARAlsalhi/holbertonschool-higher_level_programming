#!/usr/bin/env python3
"""Defines an abstract Animal class and its subclasses."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract Animal class."""

    @abstractmethod
    def sound(self):
        """Return the sound of the animal."""
        pass


class Dog(Animal):
    """Dog class that inherits from Animal."""

    def sound(self):
        """Return the dog sound."""
        return "Bark"


class Cat(Animal):
    """Cat class that inherits from Animal."""

    def sound(self):
        """Return the cat sound."""
        return "Meow"
