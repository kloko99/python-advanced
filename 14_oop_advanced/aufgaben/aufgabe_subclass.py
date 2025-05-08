"""
Aufgabe: Interface-Prüfung mit __init_subclass__

Du entwickelst eine Basisklasse 'BaseService'. Alle Subklassen sollen
eine Methode 'handle(self, request)' implementieren, um HTTP-Requests
zu verarbeiten.

Ziel:
Wenn eine Subklasse von 'BaseService' erstellt wird, soll automatisch
geprüft werden, ob die Methode 'handle(self, request)' vorhanden ist.

Deine Aufgabe:
1. Implementiere __init_subclass__ in 'BaseService', sodass beim Erben
   ein Fehler ausgelöst wird, wenn die Methode 'handle' nicht definiert ist.
2. Teste dein Interface mit zwei Subklassen:
   - eine mit gültiger 'handle'-Methode
   - eine ohne → soll TypeError werfen
3. Optional: Gib eine hilfreiche Fehlermeldung aus, z. B. mit Klassennamen.

Hinweis:
Nutze `hasattr(cls, 'handle')` oder `callable(getattr(...))` zur Prüfung.
"""


class BaseService:
    """implementiert __init_subclass__ und prüft, ob die Methode 'handle'
    existiert."""
    pass


class AuthService(BaseService):
    """Implementiert die Methode 'handle'."""

    def handle(self, request):
        print("Authentifiziere Nutzer...")


class BrokenService(BaseService):
    """Produziert Fehler, da handle() fehlt..."""
    pass  # Kein 'handle' → TypeError beim Import


# Anwendung
service = AuthService()
service.handle("dummy-request")  # → OK
