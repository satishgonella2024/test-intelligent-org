Here is the 'greet' function in Python, along with the test for it:

def greet(name):
    """
    Greets the person with the given name.
    
    Args:
        name (str): The name of the person to greet.
    
    Returns:
        str: The greeting message.
    """
    return f"Hello, {name}!"

import unittest

class TestGreet(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")
        self.assertEqual(greet("Bob"), "Hello, Bob!")

if __name__ == "__main__":
    unittest.main()