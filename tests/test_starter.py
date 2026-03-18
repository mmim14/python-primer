numbers = [1, 2, 3]
print(numbers[2])


def add(a, b):
    print("a =", a, "b =", b)
    return a + b

def test_sum():
    assert sum([1, 2, 3]) == 6

x = 5
y = 10
assert x + y == 15, "Math is broken"

