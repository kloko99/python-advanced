"""
Einführung in Pydantic (Paket zur Datenvalidierung):
https://docs.pydantic.dev/latest/

pip install pydantic
"""

import json
from pathlib import Path
from models import Wizard


BASE_DIR = Path(__file__).resolve().parent  # Pfad zu der Daten-Datei


def read_json(file: str) -> list[dict] | None:
    """Lese Json-Datei ein und liefere Liste von Dicts."""
    try:
        with open(BASE_DIR / file, encoding="utf-8") as f:
            return json.load(f)
    except IOError as e:
        print("Es ist ein Fehler beim Lesen der Datei aufgetreten.")

    return None


def main():

    gandalf = Wizard(
        id=3,
        name="Gandalf",
        age="432",
        intelligence=8378,
        magic=3,
        power=34,
        type="wizard",
        origin="bla bla",
        history=[1, "3"],
        superPower=True,
    )

    # Json Datei auslesen und aus den Datensätzen Wizard-Objekte machen
    wizards = [Wizard(**item) for item in read_json("wizards.json")]
    print(wizards)

    # um auch nachträgliche Zuweiseung zu validieren, muss in dem Model
    # die Konfiguration angepasst werden.
    # gandalf.age = "asdfkjasöldf"
    gandalf.x = 4
    print(gandalf)


main()
