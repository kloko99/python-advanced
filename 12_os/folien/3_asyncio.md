# Asyncio in Python – Ausführliche Erklärung

## Wozu asyncio?

`asyncio` ist ein Framework für **asynchrone, nebenläufige Programmierung** in Python. Es wurde entwickelt, um „gleichzeitig“ viele I/O-gebundene Aufgaben zu bearbeiten – z. B.:

- HTTP-Anfragen an viele Server senden
- Daten von vielen Clients gleichzeitig empfangen
- Viele Dateien gleichzeitig laden/schreiben

Im Gegensatz zu echten Threads arbeitet `asyncio` **kooperativ**: Der Code gibt die Kontrolle freiwillig ab, statt durch Parallelität via Threads.

**Ziel:** Hohe Effizienz bei I/O ohne Multithreading-Overhead.

---

## Grundbegriffe

### Event Loop
Ein Scheduler, der alle Aufgaben (Coroutinen) verwaltet und ausführt. Es gibt immer genau **eine** aktive Event-Loop-Instanz pro Thread.

```python
import asyncio

async def sag_hallo():
    print("Hallo")

asyncio.run(sag_hallo())
```

### Coroutine
Funktionen, die mit `async def` deklariert werden. Sie können mit `await` andere Coroutinen aufrufen.

```python
async def warte():
    await asyncio.sleep(1)  # Gibt Kontrolle für 1 Sekunde ab
```

### await
Pausiert die aktuelle Coroutine und wartet, bis das Ergebnis da ist. So kann der Event-Loop in der Zwischenzeit andere Aufgaben erledigen.

---

## asyncio.sleep vs. time.sleep
- `time.sleep(1)` blockiert den Thread komplett.
- `await asyncio.sleep(1)` blockiert **nicht** – andere Coroutinen laufen währenddessen weiter.

---

## Tasks und Scheduling

Man kann Coroutinen in Tasks verwandeln, damit sie **parallel im Event-Loop** laufen:

```python
async def foo():
    await asyncio.sleep(1)
    print("fertig")

async def main():
    task1 = asyncio.create_task(foo())
    task2 = asyncio.create_task(foo())
    await task1
    await task2

asyncio.run(main())
```

---

## Zeitgleiches Warten auf mehrere Aufgaben

### asyncio.gather

```python
async def abruf(name):
    await asyncio.sleep(1)
    return f"Ergebnis von {name}"

async def main():
    resultate = await asyncio.gather(
        abruf("Task A"),
        abruf("Task B"),
        abruf("Task C")
    )
    print(resultate)
```

---

## Fehlerbehandlung in async Code

```python
async def kann_fehl schlagen():
    raise ValueError("Fehler")

async def main():
    try:
        await kann_fehl schlagen()
    except ValueError as e:
        print("Gefangen:", e)
```

---

## Realworld-Beispiel: Gleichzeitiger Download vieler Webseiten

```python
import asyncio
import aiohttp

URLS = [
    "https://example.com",
    "https://httpbin.org/get",
    "https://python.org",
]

async def lade(session, url):
    async with session.get(url) as resp:
        text = await resp.text()
        print(f"{url}: {len(text)} Zeichen")

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [lade(session, url) for url in URLS]
        await asyncio.gather(*tasks)

asyncio.run(main())
```

### Warum das sinnvoll ist:

- Alle Anfragen laufen parallel ohne echten Threading-Overhead
- CPU bleibt frei für andere Aufgaben
- Sehr effizient bei vielen gleichartigen I/O-Aufgaben

---

## Fazit

`asyncio` ist ideal, wenn du **viele I/O-gebundene Operationen** gleichzeitig ausführen willst, ohne Multithreading-Komplexität. Es erfordert ein Umdenken, bietet aber starke Kontrolle über Nebenläufigkeit mit wenig Overhead.

