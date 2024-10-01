#!/usr/bin/env python3
# shoe.py

# shoe.py

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size  # This will call the setter
        self.condition = "New"  # Initialize the condition attribute

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        # Check if the value is not an integer
        if not isinstance(value, int):
            print("size must be an integer")
            return  # Do not set the value
        if value <= 0:
            raise ValueError("Size must be a positive number")
        self._size = value

    def cobble(self):
        """Simulates repairing the shoe."""
        print("Your shoe is as good as new!")  # Update the message to match the test requirement
        self.condition = "New"  # Set the condition to 'New' after repair
