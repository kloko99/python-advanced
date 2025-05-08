"""
Dunder Methoden
"""
class P:
    def __len__(self):
        return 42


print(dir(P()))

x = P()
print(len(x))   # repr()