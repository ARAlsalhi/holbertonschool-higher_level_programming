#!/usr/bin/env python3
"""Defines Fish, Bird, and FlyingFish classes."""


class Fish:
    """Fish class."""

    def swim(self):
        """Print swimming behavior."""
        print("The fish is swimming")

    def habitat(self):
        """Print fish habitat."""
        print("The fish lives in water")


class Bird:
    """Bird class."""

    def fly(self):
        """Print flying behavior."""
        print("The bird is flying")

    def habitat(self):
        """Print bird habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """FlyingFish class that inherits from Fish and Bird."""

    def fly(self):
        """Print flying fish flying behavior."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print flying fish swimming behavior."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Print flying fish habitat."""
        print("The flying fish lives both in water and the sky!")
