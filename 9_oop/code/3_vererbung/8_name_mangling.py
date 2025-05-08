"""
Ohne Name-Manging wird die falsche Methode aufgerufen
"""
class A:
    def __init__(self):
        self.y = 3
        self.__x = 42

    def foo(self):
        self.bar()    # ruft B.bar() auf
        self.__baz()  # ruft internes __baz auf, und nicht B.__baz

    def bar(self):
        print("A.bar") 
        print(self.y)
        

    def __baz(self):
        print("A.baz (system funktion)")
        print(self.__x)
        


class B(A):
    def bar(self):
        print("B.bar")
        print(self.y)
        # print(self.__x)  # ERROR!!!

    def __baz(self):
        print("B.baz")
        

b = B()
b.foo()
