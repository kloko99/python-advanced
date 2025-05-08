""" 
Callstack: Funktionsaufruf-Stapel
"""
def h():
    print("ich bin H")
    4 / 0


def g():
    h()


def f():
    g()


f()