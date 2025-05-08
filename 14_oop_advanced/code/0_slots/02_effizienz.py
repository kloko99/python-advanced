"""
Topic: __slots__ – Performance and Memory Efficiency

This example demonstrates how __slots__ can improve memory usage and
performance when creating many instances of a class.

We compare two classes:
1. A regular class using a dynamic __dict__
2. A class using __slots__ to restrict attributes and save memory

We will measure:
- Memory usage per instance
- Time to create 1 million instances

Note: __slots__ disables the creation of __dict__ per object,
which can significantly reduce memory usage.
"""

import time
import sys


# Class without __slots__
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Class with __slots__
class PersonWithSlots:
    __slots__ = ["name", "age"]

    def __init__(self, name, age):
        self.name = name
        self.age = age


# Memory usage comparison
p1 = Person("Anna", 30)
p2 = PersonWithSlots("Anna", 30)

# Time comparison: create 1 million instances
N = 1_000_000

start = time.perf_counter()
people = [Person("Max", 25) for _ in range(N)]
print("Without __slots__: {:.2f} seconds".format(time.perf_counter() - start))

start = time.perf_counter()
people_slots = [PersonWithSlots("Max", 25) for _ in range(N)]
print("With __slots__   : {:.2f} seconds".format(time.perf_counter() - start))


