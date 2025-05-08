"""(schwer)
Aufgabe
Schreibe ein Programm, dass die Liste mit Tupeln in ein Dict folgender Form konvertiert:

{'Frodo': {'city': 'Hobbiton',
           'first_name': 'Frodo',
           'last_name': 'Baggins',
           'salutation': 'Mr.',
           'street': 'Bag End 1'},
 'Gandalf': {'city': 'somewhere',
             'first_name': 'Gandalf',
             'last_name': 'the Grey',
             'salutation': 'Mr.',
             'street': 'Wizard street 42'},
 'Samwise': {'city': 'Hobbiton',
             'first_name': 'Samwise',
             'last_name': 'Gamgee',
             'salutation': 'Mr.',
             'street': 'Bagshot Row 2'}}

nutze dazu dict() und zip()

"""
address_list = [
    (
        "salutation",
        "first_name",
        "last_name",
        "street",
        "city",
    ),
    (
        "Mr.",
        "Frodo",
        "Baggins",
        "Bag End 1",
        "Hobbiton",
    ),
    (
        "Mr.",
        "Samwise",
        "Gamgee",
        "Bagshot Row 2",
        "Hobbiton",
    ),
    (
        "Mrs.",
        "Galadriel",
        "Elb",
        "189 Flower Gardens",
        "Lothlorien",
    ),
]
