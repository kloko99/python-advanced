# Name Mangling in Python – Schutz vor Namenskonflikten in Vererbung

**Name Mangling** ist ein Mechanismus in Python, der speziell beim Arbeiten mit Vererbung nützlich ist.  
Er sorgt dafür, dass **Attribute mit doppeltem Unterstrich am Anfang** (`__name`) **intern umbenannt werden**, um **Namenskonflikte zwischen Basisklasse und Subklasse** zu vermeiden.

---

## Was ist Name Mangling?

Wenn ein Attributname mit **zwei Unterstrichen beginnt**, aber **nicht mit zwei endet**, verändert Python den Namen intern, z. B.:

```python
class A:
    def __init__(self):
        self.__secret = "geheim"
````

Wird automatisch umgewandelt zu:

```python
self._A__secret
```

Das nennt man *Name Mangling*.

---

## Der Nutzen in der Vererbung

Stell dir vor, du baust eine Basisklasse, die interne Attribute verwendet.
Du willst verhindern, dass eine Unterklasse aus Versehen dieselben Namen verwendet und das Verhalten der Basisklasse stört.

Ohne Name Mangling kann es zu **versehentlichem Überschreiben** kommen:

```python
class Base:
    def __init__(self):
        self.__status = "OK"

class Child(Base):
    def __init__(self):
        super().__init__()
        self.__status = "ERROR"
```

### Was passiert hier?

* `Base.__status` wird zu `_Base__status`
* `Child.__status` wird zu `_Child__status`

Das bedeutet: **beide Attribute existieren unabhängig voneinander**.

➡️ **Kein Überschreiben, keine Seiteneffekte.** Das ist besonders wichtig in komplexen Klassenhierarchien oder Frameworks.

---

## Technisches Beispiel

```python
class Base:
    def __init__(self):
        self.__id = 42

class User(Base):
    def __init__(self):
        super().__init__()
        self.__id = 99

u = User()
print(u._Base__id)  # 42
print(u._User__id)  # 99
```

Beide `__id`-Felder leben getrennt. So schützt sich die Basisklasse vor unbeabsichtigten Überschreibungen.

---

## Was wird **nicht** gemangelt?

* `_name`: Nur Konvention, kein technischer Schutz.
* `__name__`: Spezialmethoden (Dunder), kein Mangling.
* Top-Level-Funktionen/Variablen: keine Veränderung durch Mangling.

---

## Fazit

* `__name` → wird zu `_Klassenname__name` (*Name Mangling*)
* Hilft, **Basisklassen robust gegen Namenskonflikte** zu machen
* Besonders nützlich bei Framework-Design, Vererbung, Erweiterbarkeit
* Kein echter Schutz vor Zugriff – aber Schutz vor unbeabsichtigtem Überschreiben

> Verwende Name Mangling gezielt, wenn du interne Attribute vor Subklassen „verstecken“ willst.

