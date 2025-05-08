""" 
Kontext Manager: Was ist ein Kontext-Manager und wie wird das 
gebaut?

Sinnvoll bei Datenbank- oder Filehandles.
"""
# das with ist ein Kontext-Manager.
# with open("data.csv") as f:
#     print(f)

class ContextManager:
    def __init__(self, x, y):
        self.x = x 
        self.y = y 

    def __enter__(self):
        """Wird aufgerufen, wenn with betreten wird."""
        print("Wir betreten enter.")
        return self  # as manager

    def __exit__(self, exc_type, exc_value, exc_traceback):
        """Wird aufgerufen bevor das Programm beendet."""
        print(exc_type, exc_value, exc_traceback)
        print("Wir verlassen den Context Manager")


with ContextManager(x=1, y=2) as manager:
    print("x:", manager.x)
    print("y:", manager.y)
    7 / 0

    