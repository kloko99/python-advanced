# Testfall-Dokument: Chatbot-Klasse & helper.py (Aufgabenstellung)

Dieses Dokument enthält die Aufgabenstellung zur Implementierung von
**Tests** für die Klasse `Chatbot` sowie für begleitende
Hilfsfunktionen aus `helper.py`. Ziel ist es, mithilfe von `pytest` eine
vollständige und saubere Testabdeckung zu erstellen.

---

## Voraussetzungen
- Ihr arbeitet in einem bestehenden Python-Projekt mit folgender Struktur:

```
chatbot_project/
├── chatbot
    ├── bot.py           # enthält die Klasse Chatbot
    ├── helper.py        # enthält Hilfsfunktionen wie clean_message, count_words
├── tests 
    ├── test_chatbot.py  # hier sollen eure Tests für Chatbot hinein
    ├── test_helper.py   # hier kommen eure Tests für helper.py hinein

Die Tests werden wie folgt in Projektroot ausgeführt:

python -m pytest -v
```

- `pytest` ist installiert (ggf. mit `pip install pytest`)

---

## Vorbereitung: Test-Fixture anlegen
Bevor ihr Tests schreibt, legt in `test_chatbot.py` eine **Fixture** an,
die für alle Tests eine Instanz des Chatbots erstellt:

> ```python
> @pytest.fixture
> def bot():
>     return Chatbot("TestBot")
> ```

Diese Fixture `bot` wird dann automatisch an eure Testfunktionen übergeben, 
und kann als Parameter verwendet werden.

---

## Zu implementierende Tests

### Teil 1: Tests für `Chatbot` (in `test_chatbot.py`)

1. **Begrüßung testen**
    - Methode: `greet()`
    - Erwartung: gibt Begrüßungstext mit Bot-Namen zurück

2. **API-Aufruf simulieren (mocken)**
    - Methode: `ask_api(msg)`
    - Simuliere verschiedene Rückgabecodes (z. B. 200, 500) mit `patch()`
    - Erwartung:
        - bei 200: "Antwort empfangen für ..."
        - bei 500: "Fehler: Antwortcode 500"

3. **Verlauf speichern**
    - Methode: `remember(text)`
    - Erwartung: `text` wird in `self.history` aufgenommen

4. **Verlauf durchsuchen**
    - Methode: `has_seen(keyword)`
    - Erwartung: gibt `True`, wenn das Keyword im Verlauf enthalten ist

5. **Längenanalyse (parametrisierter Test)**
    - Methode: `respond_length_hint(text)`
    - Erwartung: kurze Nachricht → Hinweis, lange Nachricht → Bestätigung

6. **Nachricht über Index abrufen**
    - Methode: `get_from_history(index)`
    - Erwartung: gibt gespeicherte Nachricht zurück

7. **Fehler bei ungültigem Index**
    - Methode: `get_from_history(index)`
    - Erwartung: bei ungültigem Index wird `IndexError` ausgelöst
    - Nutzt `pytest.raises(..., match=...)`

---

### Teil 2: Tests für `helper.py` (in `test_helper.py`)

8. **Text bereinigen**
    - Funktion: `clean_message(text)`
    - Erwartung: Leerzeichen werden entfernt, alles ist klein geschrieben

9. **Wörter zählen (parametrisiert)**
    - Funktion: `count_words(text)`
    - Erwartung: gibt Anzahl der Wörter im Text zurück
    - Verwendet `@pytest.mark.parametrize` für mehrere Beispiele

---

## Tipps für die Umsetzung
- Benennt eure Testfunktionen sinnvoll, z. B. `test_remember_speichert_text()`
- Beginnt jede Funktion mit `test_`, damit `pytest` sie erkennt
- Nutzt `assert` zur Überprüfung der Rückgabewerte oder Ausnahmen
- Importiert nötige Module (`pytest`, `Chatbot`, `helper`, `patch`, etc.)

---

## Tests ausführen
Im Terminal im Projektverzeichnis:

```
python -m pytest -v
```
Das zeigt euch alle Tests und ob sie erfolgreich waren oder fehlgeschlagen sind.


