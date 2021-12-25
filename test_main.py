from unittest import TestCase

def a():
    return 1, 2

b = []

b = a()
c = b[0]
d = b[1]

print(b, c, d)