"""
Thema: IntEnum – Aufzählung mit Integer-Werten in Python

`IntEnum` ist eine spezielle Form von `Enum` aus dem Modul `enum`.
Im Gegensatz zur normalen `Enum`-Klasse erben die Mitglieder von
`IntEnum` zusätzlich von `int` und verhalten sich dadurch wie
ganzzahlige Werte.

Das bedeutet:
- IntEnum-Mitglieder sind echte `int`-Werte
- Sie können direkt mit Ganzzahlen verglichen werden
- Sie können als Zahlen gespeichert oder übergeben werden

Beispiel:

    from enum import IntEnum

    class Priority(IntEnum):
        LOW = 1
        MEDIUM = 2
        HIGH = 3

    print(Priority.HIGH)        # 3
    print(Priority.HIGH.value)  # 3
    print(Priority.HIGH == 3)   # ✅ True – Vergleich mit int funktioniert

Wann verwendet man IntEnum?
- Wenn man Werte an APIs übergeben muss, die Integer erwarten
- Wenn man Enum-Mitglieder sortieren oder numerisch verarbeiten will
- Wenn man klare Konstanten mit numerischer Bedeutung benötigt (z. B. Statuscodes)

Achtung:
- Im Gegensatz zu `Enum` kann `IntEnum` unbeabsichtigte Gleichheit mit reinen ints erzeugen.
- `Enum` ist die sicherere Wahl, wenn keine numerischen Operationen nötig sind.
"""
