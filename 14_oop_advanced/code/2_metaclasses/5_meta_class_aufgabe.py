"""
Aufgabe: Metaklasse – Methoden abhängig vom wizardy-Typ einfügen

In diesem Beispiel entscheidet die Metaklasse WizardMeta beim Erzeugen
der Klasse anhand des Attributs `wizardy`, ob Methoden wie `throw()`
oder `summon()` eingebaut werden.

Nur passende Methoden werden der Klasse hinzugefügt:
- wizardy == "light" → erhält throw()
- wizardy == "conjure" → erhält summon()
- cast_spell() ist immer vorhanden

Die Konfiguration erfolgt über Schlüsselwörter beim Klassendefinitionszeitpunkt.
"""

# --- Methoden, die eingebaut werden können ---


def throw(self):
    return "Fire"


def summon(self, monster):
    return f"Summon {monster}"


def cast_spell(self):
    return f"Zap! (Mana: {self.mana})"


class WizardMeta(type):
    """Metaklasse für Zauberer-Klassen."""

    pass


# --- Klassen mit spezifiziertem Typ über Metaclass ---
class LightWizard(metaclass=WizardMeta, wizardy="light", mana=100):
    def __init__(self):
        pass


class ConjureWizard(metaclass=WizardMeta, wizardy="conjure", mana=80):
    def __init__(self):
        pass


# --- Tests ---
lw = LightWizard()
print("LightWizard:")
print("  cast_spell:", lw.cast_spell())  # ✅ Zap! (Mana: 100)
print("  throw:     ", lw.throw())  # ✅ Fire
# print("  summon:    ", lw.summon("Wolf")) # ❌ AttributeError

cw = ConjureWizard()
print("ConjureWizard:")
print("  cast_spell:", cw.cast_spell())  # ✅ Zap! (Mana: 80)
print("  summon:    ", cw.summon("Dragon"))  # ✅ Summon Dragon
# print("  throw:     ", cw.throw())            # ❌ AttributeError
