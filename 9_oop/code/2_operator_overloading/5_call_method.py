"""
Thema: __call__ – Objekte wie Funktionen aufrufen

Mit der Methode __call__(self, ...) kann ein Objekt wie eine Funktion
verwendet werden. Das bedeutet: Instanzen einer Klasse können direkt
aufgerufen werden, z. B. mit obj(...), wenn __call__ definiert ist.

"""
class Collect:
    def __init__(self, values):
        self.values = values
    
    def __call__(self, filepath):
        """Wird immer aufgerufen, wenn das Objekt gecalled wird."""
        print(self.values)
        print(filepath)


c = Collect(["Vanille", "Schoko"])
c(filepath="x.txt")