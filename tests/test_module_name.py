Here are the test cases for the 'greet' function in Python:

import unittest

def greet(name):
    if not isinstance(name, str):
        raise TypeError("Name must be a string")
    if not name:
        return "Hello, stranger!"
    return f"Hello, {name}!"

class TestGreet(unittest.TestCase):
    def test_greet_with_name(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")

    def test_greet_with_empty_string(self):
        self.assertEqual(greet(""), "Hello, stranger!")

    def test_greet_with_non_string_type(self):
        with self.assertRaises(TypeError):
            greet(123)

    def test_greet_with_none(self):
        with self.assertRaises(TypeError):
            greet(None)

if __name__ == '__main__':
    unittest.main()

This code includes the following test cases:

1. `test_greet_with_name`: Checks that the function correctly greets a person with a given name.
2. `test_greet_with_empty_string`: Checks that the function correctly handles an empty string input.
3. `test_greet_with_non_string_type`: Checks that the function correctly raises a `TypeError` when a non-string type is passed as the `name` argument.
4. `test_greet_with_none`: Checks that the function correctly raises a `TypeError` when `None` is passed as the `name` argument.

The `greet` function itself is also included in the code. It checks the input type and returns the appropriate greeting message.