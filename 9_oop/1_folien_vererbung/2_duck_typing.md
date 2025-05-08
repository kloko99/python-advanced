# Polymorphie vs. Duck Typing in Python

Polymorphie und Duck Typing sind zwei Konzepte in Python, die Flexibilität und
Erweiterbarkeit im Code ermöglichen, jedoch auf unterschiedliche Weise. Schauen
wir uns jedes Konzept an und betrachten die Unterschiede.

# Polymorphie

Polymorphie erlaubt es, Objekte verschiedener Klassen als Objekte einer
gemeinsamen Superklasse zu behandeln. Dies ist ein zentrales Prinzip der
objektorientierten Programmierung(OOP) und kann auf zwei Hauptarten
implementiert werden: **vererbungsbasierte Polymorphie ** und
**Methodenüberschreibung**.

1. ** Vererbungsbasierte Polymorphie**:
   - Wenn eine Klasse von einer Basisklasse abgeleitet wird, erbt sie die
     Methoden der Basisklasse und kann sie ähnlich verwenden.
   - Dies ermöglicht es, verschiedene Unterklassen einheitlich zu behandeln,
     sofern sie von derselben Superklasse erben.

2. ** Methodenüberschreibung**:
   - Eine Unterklasse kann eine spezifische Implementierung einer Methode
     bereitstellen, die bereits in ihrer Superklasse definiert ist. Dadurch kann
     die Unterklasse eigenes Verhalten haben, während sie dennoch die allgemeine
     Schnittstelle der Superklasse beibehält.

# Beispiel für Polymorphie in Python

```python


class Tier:
    def sprich(self):
        pass


class Hund(Tier):
    def sprich(self):
        return "Wuff!"


class Katze(Tier):
    def sprich(self):
        return "Miau!"


def tier_spricht(tier: Tier):
    print(tier.sprich())


tier_spricht(Hund())   # Ausgabe: Wuff!
tier_spricht(Katze())  # Ausgabe: Miau!
```

In diesem Beispiel:

- Sowohl `Hund` als auch `Katze` erben von `Tier`, was es ermöglicht, sie als
  `Tier`-Typen zu behandeln.
- Die Methode `sprich` wird in jeder Unterklasse überschrieben, aber
  `tier_spricht` kann `sprich` auf jedem `Tier`-Subtyp aufrufen, ohne den
  spezifischen Typ zu kennen.

# Duck Typing

Duck Typing ist ein Konzept in dynamisch typisierten Sprachen wie Python, bei
dem die Eignung eines Objekts durch das Vorhandensein bestimmter Methoden und
Eigenschaften bestimmt wird, anstatt durch den tatsächlichen Typ des Objekts.
Beim Duck Typing gilt ein Objekt als geeignet für eine Operation, wenn es die
notwendigen Methoden und Attribute besitzt, unabhängig von seiner
Vererbungshierarchie.

Der Satz "Wenn es wie eine Ente aussieht und wie eine Ente quakt, dann ist es
eine Ente" beschreibt diese Idee gut. Duck Typing gilt oft als eine flexiblere
Alternative zur strikten Polymorphie, da es keine formale Klassenbeziehung
erfordert.

### Beispiel für Duck Typing in Python

```python
class Hund:
    def sprich(self):
        return "Wuff!"

class Katze:
    def sprich(self):
        return "Miau!"

class Ente:
    def sprich(self):
        return "Quak!"

def lasse_sprechen(tier):
    print(tier.sprich())

lasse_sprechen(Hund())   # Ausgabe: Wuff!
lasse_sprechen(Katze())  # Ausgabe: Miau!
lasse_sprechen(Ente())   # Ausgabe: Quak!
```

In diesem Beispiel:

- `Hund`, `Katze` und `Ente` sind keine Unterklassen einer gemeinsamen
  Superklasse.
- `lasse_sprechen` erfordert nicht, dass `tier` ein bestimmter Typ ist; es ruft
  lediglich `sprich` auf dem übergebenen Objekt auf und nimmt an, dass jedes
  gültige „Tier“ eine `sprich`-Methode hat.
- Diese Flexibilität ermöglicht es, eine größere Vielfalt von Objekten mit
  `lasse_sprechen` zu verwenden, ohne eine Vererbungshierarchie durchzusetzen.

## Hauptunterschiede

| Aspekt                | Polymorphie                                         | Duck Typing                                                      |
| --------------------- | --------------------------------------------------- | ---------------------------------------------------------------- |
| **Typprüfung**        | Basierend auf Klassenvererbung                      | Basierend auf Methoden-Existenz                                  |
| **Implementierung**   | Verwendet normalerweise eine gemeinsame Superklasse | Benötigt keine Superklasse                                       |
| **Flexibilität**      | Weniger flexibel, erfordert Typhierarchie           | Flexibler, akzeptiert jeden Typ mit der benötigten Methode       |
| **Statische Analyse** | Leichter für statische Typprüfung                   | Schwieriger für statische Analyse aufgrund der dynamischen Natur |

## Zusammenfassung

- **Polymorphie** ist strukturierter und erzwingt eine Typbeziehung, was
  nützlich ist, wenn man ein formales, konsistentes Verhalten über verschiedene
  Typen hinweg gewährleisten möchte.
- **Duck Typing** ist flexibler und beruht auf dem Verhalten des Objekts statt
  auf seinem spezifischen Typ. Es ist nützlich in Situationen, in denen man
  keine strikte Typhierarchie erzwingen möchte.

Beide Ansätze haben ihren Platz in Python: Polymorphie wird oft für
strukturierte OOP-Designs verwendet, während Duck Typing die dynamische Natur
von Python für lockerer strukturierte Codebasis nutzt.
