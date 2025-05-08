"""
Representation of Python Data Types

repr => interne Funktion, die __repr__() aufruft.
"""

print(repr("hello")) # 'hello'
print("hello") # hello

x = [1, 2, "34"]
print(repr(x))
print(str(x))

name="Bob"
print(f"{name!r}")  # !r => mache repr(name)