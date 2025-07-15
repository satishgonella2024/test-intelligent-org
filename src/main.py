Here is the 'greet' function and test cases in Python:

def greet(name):
    """
    Greets the person with the given name.
    
    Args:
        name (str): The name of the person to greet.
    
    Returns:
        str: The greeting message.
    """
    return f"Hello, {name}!"

def test_greet():
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Bob") == "Hello, Bob!"
    assert greet("") == "Hello, !"
    assert greet(None) == "Hello, None!"

if __name__ == "__main__":
    test_greet()
    print("All tests passed!")