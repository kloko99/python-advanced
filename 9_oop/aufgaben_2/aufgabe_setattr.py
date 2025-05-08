"""
setattr (Schwer)
Wir haben eine Klasse LineItem gegeben. Erstelle LineItem-Objekte und speichere
sie in einer Liste line_items. Achte in __init__ darauf, dass die Werte in
**kwargs übergeben werden und erstelle dynamisch die Attribute.
Es muss __repr__ implementiert sein, wie unten gezeigt.
"""


class LineItem:
    def __init__(self, **kwargs): 
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        value_list = ", ".join([f"{k}={v!r}" for k, v in vars(self).items()])
        return f"{self.__class__.__name__}({value_list})"   # LineItem(id=3, name='Pencil')


lines = [
    {
        "id": 3,
        "name": "Pencil Geha",
        "style": "bold",
        "color": "black",
    },
    {
        "id": 13,
        "name": "Pencil Geha Professional",
        "style": "bold",
        "color": "red",
    },
    {
        "id": 23,
        "name": "Parker Chef",
        "style": "thin",
        "color": "silver",
        "al": 34
    },
]


line_items = []
for item in lines:
    line_items.append(LineItem(**item))


print(line_items)

# Result:
# [<LineItem(id=3,name='Pencil Geha',style='bold',color='black')>, <LineItem(id=13,name='Pencil Geha Professional',style='bold',color='red')>, <LineItem(id=23,name='Parker Chef',style='thin',color='silver')>]
# def fn(a):
#     print(a)


# x = {"a": 3, "b": 3}
# fn(**x)  # fn(a=3, b=3)

# Join-Methode: alles zu einem STring machen
names = ["bob", "alice", "grumpe"]
names = ", ".join(names)
print(names)