"""Basic Stack Implementation.

Aufgabe:
Erstelle für die Klasse Stack einen Doctest und führe den Test
auf der Kommandozeile aus:

python -m doctest 2_stack.py

Test:
push, pop, peek, is_empty, size
pop() auf einem Leeren Stack löst eine Exception aus.

IndexError: pop from empty list
"""


class Stack:
    """Basic Stack Implementation."""

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return not bool(self.items)

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    import doctest

    stack_int = Stack()
    stack_int.push(1)
    stack_int.push(2)

    doctest.testmod()
    # nur wenn Fehler auftritt, gibt es einen Output
