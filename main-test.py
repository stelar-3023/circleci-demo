# Import the add_number function from main.py, and assert that it returns the correct value.
from main import add_number

def test_add():
    assert add_number(1, 2) == 3
    print("Test passed!")

if __name__ == "__main__":
    test_add()