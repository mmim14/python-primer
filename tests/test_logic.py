def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def is_even(n):
    """Return True if n is an even number."""
    return n % 2 == 0


def reverse_string(s):
    """Return the reversed string."""
    return s[::-1]


# Test cases
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_is_even():
    assert is_even(4) is True
    assert is_even(3) is False
    assert is_even(0) is True


def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("a") == "a"
    assert reverse_string("") == ""