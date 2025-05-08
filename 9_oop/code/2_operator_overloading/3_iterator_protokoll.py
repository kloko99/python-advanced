"""
Thema: Das Iterator-Protokoll in Python

Das Iterator-Protokoll beschreibt, wie Objekte in Python iterierbar
gemacht werden können. Ein Objekt gilt als Iterator, wenn es:

1. Die Methode __iter__() besitzt, die das Objekt selbst zurückgibt.
2. Die Methode __next__() implementiert, die das nächste Element
   zurückgibt oder StopIteration auslöst, wenn keine Elemente mehr da sind.

Iteratoren ermöglichen die Nutzung in for-Schleifen, Generatoren,
List-Comprehensions und allen anderen iterierbaren Kontexten.

Dieses Protokoll ist zentral für die Arbeit mit Sequenzen und Streams.
"""
class PortFolio:
    def __init__(self):
        self.holdings: dict = {}  # key = ticker, number of shares

    def buy(self, ticker: str, shares: int):
        """Füge n shares dem Ticker hinzu."""
        self.holdings[ticker] = self.holdings.get(ticker, 0) + shares

    def __iter__(self):
        """iter muss einen Iterator zurückgeben."""
        return iter(self.holdings.items())


p = PortFolio()
p.buy("EVILCORP", 3)
p.buy("BMW", 42)
p.buy("BMW", 43)

# Stock-Ticker und Anteile iterativ ausgeben
for stock, shares in p:
    print(stock, shares)


class Club:
    """einfache Fussball-Club Klasse."""
    def __init__(self, name):
        self.name = name
        self.players = []
        self.pos = 0  # benötigen wir für den Iterator
        
    def add(self, player):
        self.players.append(player)
    
    def __len__(self):
        return len(self.players)

    def __iter__(self):
        """liefert einen Iterator. In diesem Fall ist das Objekt selbst 
        der Iterator. Dazu muss die Klasse __next__() implementieren."""
        return self
    
    def __next__(self):
        """Liefert immre das nächste Objekt.
        Ein Iterator muss einen Stop-Iteration Error auslösen, falls er 
        verbraucht ist.
        """
        try:
            player = self.players[self.pos]
        except IndexError:
            self.pos = 0  # Zähler wieder zurücksetzen
            raise StopIteration
        self.pos += 1
        return player




st_pauli = Club("St. Pauli")
st_pauli.add("Thomas K.")
st_pauli.add("Peter P.")

for player in st_pauli:
    print(player)

for player in st_pauli:
    print(player)