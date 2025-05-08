# Einführung in Slots

In Python ist jede Objektinstanz mit Standardfunktionen und -attributen vordefiniert. Python verwendet zum Beispiel ein Dictionary, um die Instanzattribute eines Objekts zu speichern. Dies hat viele Vorteile, z. B. können wir zur Laufzeit neue Attribute hinzufügen. Dieser Komfort hat jedoch seinen Preis.

Dictionary können einen großen Teil des Speichers beanspruchen, vor allem wenn wir viele Instanzobjekte mit einer großen Anzahl von Attributen haben. Wenn die Leistung und Speichereffizienz des Codes entscheidend sind, können wir den Komfort von Dictionary gegen __slots__ eintauschen.

In diesem Tutorium werden wir uns ansehen, was __slots__ sind und wie man sie in Python benutzt. Wir werden auch die Nachteile der Verwendung von __slots__ diskutieren und ihre Leistung im Vergleich zu typischen Klassen, die ihre Instanzattribute in Dictionaries speichern, betrachten.


## Was sind __slots_ und wie verwendet man sie?

Slots sind Klassenvariablen, denen eine Zeichenkette, eine Iterable oder eine Folge von Zeichenketten mit den Namen der Instanzvariablen zugewiesen werden kann. Wenn Sie Slots verwenden, benennen Sie die Instanzvariablen eines Objekts `im Voraus` und verlieren die Möglichkeit, sie dynamisch hinzuzufügen.

Eine Objektinstanz, die Slots verwendet, verfügt nicht über ein eingebautes Dictionary. Dadurch wird mehr Platz gespart und der Zugriff auf die Attribute ist schneller.

Schauen wir uns das in Aktion an. Betrachten wir diese reguläre Klasse:

class PlayerWithoutSlots():
    game = "Monopoly"

    def __init__(self, name, location):
        self.name = name
        self.location = location

ohne_slots = PlayerWithoutSlots('Freddy', 'Köln')
print(ohne_slots.__dict__) 

In dem obigen Ausschnitt:

    game ist eine Klassenvariable
    name und location sind Instanzvariablen

Während jede Objektinstanz der Klasse erstellt wird, wird ein dynamisches Dictionary unter dem Attribut name als __dict__ zugewiesen, das alle beschreibbaren Attribute eines Objekts enthält. Die Ausgabe des obigen Codeschnipsels ist:

    print(ohne_slots.__dict__) 
    {'name': 'Freddy', 'location': 'Köln'}

jetzt nutzen wir Slots

class PlayerWithoutSlots():
    game = "Monopoly"
    __slots__ = ('name', 'location')

    def __init__(self, name, location):
        self.name = name
        self.location = location

mit_slots = PlayerWithoutSlots('Freddy', 'Köln')
print(mit_slots.__dict__) # ERROR

Das Dictionary fehlt, da wir __slots__ nutzen.


