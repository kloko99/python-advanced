# Python Reguläre Ausdrücke (RegEx) Tutorial

Reguläre Ausdrücke (RegEx) sind eine mächtige Methode zur Mustererkennung und Textverarbeitung. In Python wird dies durch das `re` Modul ermöglicht.

## Grundlagen

Ein regulärer Ausdruck ist eine spezielle Textzeichenfolge, die ein Suchmuster definiert. Python's `re` Modul bietet eine Reihe von Funktionen, um mit RegEx zu arbeiten.

### Wichtige Funktionen:

- `re.search()`: Überprüft, ob das Muster irgendwo im Text vorkommt.
- `re.match()`: Überprüft, ob das Muster am Anfang des Textes vorkommt.
- `re.findall()`: Findet alle Vorkommen des Musters im Text.
- `re.sub()`: Ersetzt Vorkommen des Musters im Text.

### Einfaches Beispiel

```python
import re

pattern = r"Apfel"
string = "Ich habe einen Apfel."

match = re.search(pattern, string)

if match:
    print("Muster gefunden!")
else:
    print("Kein Muster gefunden.")
```

## Metazeichen

Metazeichen sind das Herzstück von RegEx. Einige der wichtigsten Metazeichen sind:

- `.` (Punkt): Steht für jedes Zeichen außer für einen Zeilenumbruch.
- `^`: Das Muster muss am Anfang der Zeichenfolge stehen.
- `$`: Das Muster muss am Ende der Zeichenfolge stehen.
- `*`: Das vorherige Zeichen kann null- oder mehrmals vorkommen.
- `+`: Das vorherige Zeichen muss mindestens einmal vorkommen.
- `?`: Das vorherige Zeichen kann null- oder einmal vorkommen.
- `{}`: Eine spezifizierte Anzahl an Wiederholungen des vorherigen Zeichens.

### Beispiel mit Metazeichen

```python
pattern = r"Apf.l"
string = "Ich habe einen Apfel, eine Apfel, einen Apfl."

matches = re.findall(pattern, string)
print(matches)  # ['Apfel', 'Apfel']
```

## Zeichensätze

Zeichensätze, definiert in `[]`, erlauben es, eine Menge von Zeichen anzugeben, von denen eines im Text vorkommen soll.

### Beispiel für Zeichensätze

```python
pattern = r"Apf[aeiou]l"
string = "Apfel, Apfal, Apfil, Apfol, Apful"

matches = re.findall(pattern, string)
print(matches)  # ['Apfel', 'Apfal', 'Apfil', 'Apfol', 'Apful']
```

## Escape-Zeichen

Das Backslash-Symbol `\` wird verwendet, um spezielle Zeichen zu "escapen", also ihre spezielle Bedeutung aufzuheben.

### Beispiel für Escape-Zeichen

```python
pattern = r"Apfel\."
string = "Ich mag den Apfel."

match = re.search(pattern, string)
if match:
    print("Gefunden:", match.group())
else:
    print("Nicht gefunden.")
```

## Gruppen und Benennung von Gruppen

In regulären Ausdrücken können Sie Gruppen mit `()` definieren. Benannte Gruppen verwenden die Syntax `(?P<name>...)`.

### Beispiel für Gruppen

```python
pattern = r"(\d{2})-(\d{2})-(\d{4})"
string = "Heute ist der 25-01-2024."

match = re.search(pattern, string)
if match:
    print("Tag:", match.group(1))
    print("Monat:", match.group(2))
    print("Jahr:", match.group(3))
```

## Flags

Flags ändern das Verhalten des regulären Ausdrucks. Zum Beispiel macht das Flag `re.IGNORECASE` die Suche unempfindlich gegenüber Groß- und Kleinschreibung.

### Beispiel mit Flags

```python
pattern = r"apfel"
string = "Ich liebe Äpfel!"

matches = re.findall(pattern, string, re.IGNORECASE)
print(matches)  # ['Äpfel']
```

## Quantoren

Quantoren steuern, wie oft ein Zeichenmuster in einem String vorkommt.

### `?` – Null oder Einmal

```python
import re
pattern = r"colou?r"
string = "color and colour"
matches = re.findall(pattern, string)
print(matches)  # ['color', 'colour']
```

### `*` – Null oder Mehrmals

```python
pattern = r"go*gle"
string = "ggle, gogle, google, goooggggle"
matches = re.findall(pattern, string)
print(matches)  # ['ggle', 'gogle', 'google', 'goooggggle']
```

### `+` – Einmal oder Mehrmals

```python
pattern = r"go+gle"
string = "ggle, gogle, google, goooggggle"
matches = re.findall(pattern, string)
print(matches)  # ['gogle', 'google', 'goooggggle']
```

### `{n}`, `{n,}`, `{min,max}` – Spezifische Anzahl

```python
pattern = r"go{2,3}gle"
string = "ggle, gogle, google, goooggggle"
matches = re.findall(pattern, string)
print(matches)  # ['google', 'goooggggle']
```

## Anker

Anker bestimmen die Position im String, an der das Muster übereinstimmen soll.

### `^` – Am Anfang eines Strings

```python
pattern = r"^Hallo"
string = "Hallo Welt"
match = re.match(pattern, string)
print(bool(match))  # True
```

### `$` – Am Ende eines Strings

```python
pattern = r"Ende$"
string = "Alles hat ein Ende"
match = re.search(pattern, string)
print(bool(match))  # True
```

### `\b` und `\B` – Wortgrenzen

```python
pattern = r"\bJa\b"
string = "Ja, das ist richtig"
matches = re.findall(pattern, string)
print(matches)  # ['Ja']
```

## Identifizierer

Identifizierer sind spezielle Zeichen oder Sequenzen, die bestimmte Zeichentypen repräsentieren.

### `.` – Irgendein Zeichen (außer Zeilenumbruch)

```python
pattern = r"a.b"
string = "acb aeb a\nb"
matches = re.findall(pattern, string)
print(matches)  # ['acb', 'aeb']
```

### `[a-z0-9]` – Zeichenklassen

```python
pattern = r"[a-z0-9]"
string = "Apfel123"
matches = re.findall(pattern, string)
print(matches)  # ['p', 'f', 'e', 'l', '1', '2', '3']
```

### `[abc]` – Zeichenmengen

```python
pattern = r"[abc]"
string = "apple, berry, cherry"
matches = re.findall(pattern, string)
print(matches)  # ['a', 'b', 'c', 'b', 'c']
```

### `\d`, `\D` – Zahlen und Nicht-Zahlen

```python
pattern = r"\d"
string = "Zahl: 123, Buchstaben: abc"
matches = re.findall(pattern, string)
print(matches)  # ['1', '2', '3']
```

### `\w`, `\W` – Wortzeichen und Nicht-Wortzeichen

```python
pattern = r"\w"
string = "abc123!@#"
matches = re.findall(pattern, string)
print(matches)  # ['a', 'b', 'c', '1', '2', '3']
```

### `\s`, `\S` – Whitespace und Nicht-Whitespace

```python
pattern = r"\s"
string = "Dies ist ein Test."
matches = re.findall(pattern, string)
print(matches)  # [' ', ' ', ' ', ' ']
```

### `(abc)` – Gruppen

```python
pattern = r"(abc)"
string = "abc123abc"
matches = re.findall(pattern, string)
print(matches)  # ['abc', 'abc']
```
