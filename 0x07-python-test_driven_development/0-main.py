#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(1, -2))
print(add_integer(-2, 1))
print(add_integer("Hello", 1))
print(add_integer(100.3, "Hello"))
print(add_integer(400.3, 2))
print(add_integer(-2, 400.2))
print(add_integer([2, 4, 8]))

try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)
