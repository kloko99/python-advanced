"""
Set Comprehensions ermöglichen das Erzeugen von Mengen (Sets) auf
kompakte Weise. Sie ähneln List Comprehensions, liefern aber eine
ungeordnete Sammlung eindeutiger Elemente.

In diesem Beispiel werden Set Comprehensions anhand eines realen
Szenarios verwendet: Duplikate aus Daten entfernen und Filtern
von Zeichen in Texten.
"""

# Liste von Benutzereingaben mit Duplikaten
emails = [
    "max@sensei.com",
    "lara@cthullu.com",
    "max@peaches.com",
    "john@xanadoo.com",
    "lara@firefly.com",
]

# Beispiel: Nur Domains extrahieren und in ein Set speichern
unique = {email for email in emails}
print(type(unique))

unique = set(emails)  # direkt in Set umwandeln, um doppelte Einträge zu vermeiden

# Zeichenfilter: Nur eindeutige Buchstaben extrahieren aus einem Text
text = "Hallo, Welt! 123 :)"
zeichen = {c for c in text if c.isalpha()}   # set([c for c in text if c.isalpha])
print(zeichen)


# Aufgabe: Gegeben ist eine Liste von Produktnamen (mit Duplikaten),
# erstelle ein Set mit allen eindeutig vorkommenden Namen (caseinsensitiv).
# Ergebnis: {'banane', 'kiwi', 'apfel'}
produkte = ["Apfel", "Banane", "Apfel", "Kiwi", "BANANE"]


# Aufgabe: Finde alle Buchstaben, die sowohl in Text A als auch in
# Text B vorkommen, mit Hilfe von Set Comprehensions
text_a = "Python ist -?=- toll"
text_b = "Programmieren macht Spaß!!!"

# Aufgabe: Löse das Problem mit Schnittmengen
# Finde alle Buchstaben, die sowohl in Text A, B  und C vorkommen
text_a = "Python ist -?=- e toll"
text_b = "Programmieren!! macht Spaß!"
text_c = "Zellüberlaufen Psi?!"
