"""
Thema: Enums in Python – Aufzählungstypen definieren

Ein Enum (Abkürzung für *enumeration*) ist ein spezieller Datentyp,
mit dem man symbolische Namen für feste Werte definieren kann.
So entstehen **konstante, benannte Werte**, die sich z. B. besser
lesen, warten und typisieren lassen als einfache Strings oder Zahlen.

Python bietet dafür das Modul `enum` mit der Basisklasse `Enum`.

Vorteile:
- besser lesbarer Code (z. B. Color.RED statt "red")
- feste Wertemengen, z. B. Status, Typen, Kategorien
- Vergleichbarkeit, Iteration, Typsicherheit
- zentrale Definition der erlaubten Werte

Beispiel:

    from enum import Enum

    class Status(Enum):
        PENDING = "pending"
        PAID = "paid"
        CANCELED = "canceled"

    print(Status.PENDING.value)   # "pending"
    print(Status["PAID"])         # Status.PAID

Enums sind unveränderlich, vergleichbar und ideal, um z. B. Zustände,
Rollen, Aktionen oder Konfigurationsmodi konsistent abzubilden.
"""
from enum import Enum, IntEnum, StrEnum, auto


class Days(Enum):
    SUN = auto()   # 1
    MON = auto()
    TUE = auto()


print(Days.SUN.value)  # 1



class HTTPStatus(IntEnum):
    BAD_REQUEST = 400
    NOT_FOUND = 404
    SERVER_ERROR = 500 


response = 404
if response == HTTPStatus.NOT_FOUND:
    print("Response:", HTTPStatus.NOT_FOUND)       # 404
    print("Response:", HTTPStatus.NOT_FOUND.name)  # NOT_FOUND


