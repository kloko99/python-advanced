""" 
Datei auslesen und mit Yield Zurückgeben. 
Die Größe der Datei datapoints.csv spielt keine Rolle, da effizient 
über sie iteriert und nicht alles eingelesen wird.
"""
from typing import NamedTuple, Generator
from typing import TextIO
from pathlib import Path 


class DataPoint(NamedTuple):
    """Klasse für räumliche Koordinaten."""
    x: int
    y: int
    z: int 


def datapoint_reader(file: TextIO) -> Generator:
    """Iteriere über CSV-Datei und erzeuge Datapoint-Objekte."""
    for line in file:
        cols = line.strip().split(",")
        cols = list(map(int, cols))
        yield DataPoint(*cols)
        

def file_reader(filename: str) -> None:
    """Lese Datenpunkte ein und erstelle DataPoint-Objekte."""
    with open(Path(__file__).parent / filename) as f:
        for datapoint in datapoint_reader(f):
            print(datapoint)


file_reader("datapoints.csv")