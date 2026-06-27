#!/usr/bin/env python3
"""Defines a CountedIterator class."""


class CountedIterator:
    """Iterator that counts how many items have been iterated."""

    def __init__(self, iterable):
        """Initialize the iterator and counter."""
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """Return the next item and increase the counter."""
        item = next(self.iterator)
        self.count += 1
        return item

    def __iter__(self):
        """Return the iterator object itself."""
        return self

    def get_count(self):
        """Return the number of iterated items."""
        return self.count
