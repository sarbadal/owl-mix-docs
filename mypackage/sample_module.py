"""
sample_module.py

A sample Python module for demonstration purposes.
"""

class Greeter:
    """A simple greeter class."""

    def __init__(self, name):
        """
        Initialize the greeter with a name.

        :param name: Name to greet.
        """
        self.name = name

    def greet(self):
        """
        Return a greeting message.

        :return: Greeting string.
        """
        return f"Hello, {self.name}!"

def add(a, b):
    """
    Add two numbers.

    :param a: First number.
    :param b: Second number.
    :return: Sum of a and b.
    """
    return a + b