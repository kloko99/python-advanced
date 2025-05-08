"""
Thema: default_factory in @dataclass-Feldern

In Python-Datenklassen (`@dataclass`) können Standardwerte für Felder
entweder direkt mit `default=...` angegeben werden oder mit
`default_factory=...`.

`default_factory` ist besonders dann sinnvoll, wenn der Standardwert
ein **veränderbarer Datentyp** oder ein **dynamisch erzeugtes Objekt**
sein soll, z. B.:

- leere Listen oder Dictionaries
- Objekte, die zur Laufzeit erzeugt werden
- Zufallszahlen, Zeitstempel etc.

Beispiel:

    from dataclasses import dataclass, field

    @dataclass
    class Order:
        items: list[str] = field(default_factory=list)

Ohne `default_factory` würden alle Instanzen dieselbe Liste teilen –
was zu unerwartetem Verhalten führen kann.

`default_factory` nimmt eine **Funktion ohne Argumente**, die bei jeder
Instanziierung aufgerufen wird, um einen neuen Standardwert zu erzeugen.
"""
