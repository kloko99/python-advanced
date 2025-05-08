# Multiprocessing

Multiprocessing bietet eine Alternative zum Multithreading, indem es mehrere Prozesse statt Threads verwendet. Da jeder Prozess seinen eigenen Python-Interpreter und damit seinen eigenen GIL hat, ermöglicht Multiprocessing die echte parallele Ausführung von Code auf Mehrkernprozessoren.


## Einführung in das `multiprocessing`-Modul
Das `multiprocessing`-Modul in Python ermöglicht die Erstellung von separaten Prozessen, die parallel auf Mehrkernsystemen ausgeführt werden können. Es bietet eine API, die der des `threading`-Moduls ähnlich ist, was die Umstellung von Threading auf Multiprocessing erleichtert.

## Grundlagen von Multiprocessing

### Prozesse erstellen
Um einen neuen Prozess zu starten, verwenden Sie die `Process`-Klasse aus dem `multiprocessing`-Modul. Sie müssen die Ziel-Funktion angeben, die vom Prozess ausgeführt werden soll.

```python
from multiprocessing import Process

def meine_funktion(name):
    print(f'Prozess {name} läuft')

if __name__ == '__main__':
    p = Process(target=meine_funktion, args=('Python',))
    p.start()
    p.join()  # Warten auf die Beendigung des Prozesses
```

### Daten zwischen Prozessen austauschen
Das `multiprocessing`-Modul bietet mehrere Möglichkeiten, um Daten zwischen Prozessen auszutauschen, z.B. über Queues oder Pipes.

#### Verwendung von Queues
Queues ermöglichen es Ihnen, Thread- und Prozess-sichere FIFO-Queues für den Datenaustausch zwischen Prozessen zu erstellen.

```python
from multiprocessing import Process, Queue

def worker(q):
    q.put("Hallo von einem Prozess!")

if __name__ == '__main__':
    q = Queue()
    p = Process(target=worker, args=(q,))
    p.start()
    p.join()
    print(q.get())  # Ausgabe: Hallo von einem Prozess!
```

### Pool von Prozessen
Ein Pool von Prozessen kann verwendet werden, um eine feste Anzahl von Prozessen für die Ausführung mehrerer Aufgaben zu allozieren. Dies ist nützlich, um die Ressourcennutzung auf Systemen mit vielen Kernen zu optimieren.

```python
from multiprocessing import Pool

def meine_funktion(x):
    return x * x

if __name__ == '__main__':
    with Pool(4) as p:
        print(p.map(meine_funktion, range(9)))
```

## Vorteile von Multiprocessing
- **Echte Parallele Ausführung**: Erlaubt die Nutzung von Mehrkernprozessoren, um Aufgaben parallel auszuführen.
- **Umgehung des GIL**: Jeder Prozess hat seinen eigenen Python-Interpreter und GIL, was bedeutet, dass der GIL die parallele Ausführung nicht behindert.

## Überlegungen
- **Ressourcennutzung**: Prozesse sind schwerwiegender als Threads und können mehr Systemressourcen verbrauchen.
- **Interprozesskommunikation**: Der Austausch von Daten zwischen Prozessen kann komplexer sein als bei der Verwendung von Threads.

## Zusammenfassung
Multiprocessing in Python bietet eine leistungsstarke Alternative zu Threading, insbesondere für CPU-bound Aufgaben, die von echter paralleler Ausführung profitieren. Durch die Nutzung des `multiprocessing`-Moduls können Entwickler Anwendungen erstellen, die die volle Leistungsfähigkeit moderner Mehrkernprozessoren ausschöpfen.


Nachdem wir das Thema Multiprocessing behandelt haben, ist es an der Zeit, uns mit dem **ProcessPoolExecutor** zu befassen, der eine High-Level-Schnittstelle für die Ausführung von Prozessen parallel bietet. Der ProcessPoolExecutor ist Teil des `concurrent.futures`-Moduls und ermöglicht es, Aufgaben auf eine Pool von Prozessen zu verteilen, was besonders nützlich für CPU-intensive Aufgaben ist.

---

# ProcessPoolExecutor

## Einführung
Der `ProcessPoolExecutor` ist eine Implementierung der Executor-Schnittstelle, die Prozesse anstelle von Threads verwendet, um asynchrone Ausführungen zu ermöglichen. Dies umgeht den Global Interpreter Lock (GIL) und ermöglicht echte parallele Ausführung auf Mehrkernsystemen.

## Grundlagen des ProcessPoolExecutors

### Ein Executor-Objekt erstellen
Um einen `ProcessPoolExecutor` zu verwenden, erstellen Sie zunächst eine Instanz des Executors. In der Regel verwenden Sie den `ProcessPoolExecutor` innerhalb eines Kontextmanagers, um sicherzustellen, dass alle Prozesse ordnungsgemäß beendet werden.

```python
from concurrent.futures import ProcessPoolExecutor

with ProcessPoolExecutor(max_workers=4) as executor:
    # Hier werden Tasks hinzugefügt
    pass
```

### Tasks einreichen
Mit der `submit()`-Methode können Sie einzelne Funktionen zur asynchronen Ausführung einreichen. Die Methode gibt ein `Future`-Objekt zurück, das das Ergebnis der Funktion darstellt.

```python
def berechne(x):
    return x * x

with ProcessPoolExecutor(max_workers=4) as executor:
    future = executor.submit(berechne, 4)
    ergebnis = future.result()
    print(ergebnis)  # Ausgabe: 16
```

### Mehrere Tasks gleichzeitig ausführen
Um mehrere Aufgaben gleichzeitig auszuführen, können Sie die `map()`-Methode verwenden, die eine Sequenz von Werten entgegennimmt und die Funktion parallel für jeden Wert ausführt.

```python
with ProcessPoolExecutor(max_workers=4) as executor:
    ergebnisse = executor.map(berechne, [1, 2, 3, 4, 5])
    for ergebnis in ergebnisse:
        print(ergebnis)
```

## Vorteile des ProcessPoolExecutors
- **Echte parallele Ausführung**: Nutzt Mehrkernprozessoren effektiv für CPU-bound Aufgaben.
- **Einfache API**: Bietet eine einfache und konsistente Schnittstelle für die asynchrone Programmierung.
- **Flexibilität**: Erlaubt es, die Anzahl der Worker-Prozesse anzupassen, um die Ressourcennutzung zu optimieren.

## Überlegungen zur Verwendung
- **Overhead**: Das Starten von Prozessen kann mehr Overhead verursachen als das Starten von Threads.
- **Datenübertragung**: Objekte, die zwischen dem Hauptprozess und den Worker-Prozessen übertragen werden, müssen serialisiert werden, was zusätzlichen Overhead verursachen kann.

## Zusammenfassung
Der `ProcessPoolExecutor` aus dem `concurrent.futures`-Modul ist ein mächtiges Werkzeug für die parallele Ausführung von Aufgaben in Python, besonders geeignet für CPU-intensive Aufgaben. Durch die Verwendung von Prozessen anstelle von Threads bietet er eine Möglichkeit, den GIL zu umgehen und die Leistung von Mehrkernprozessoren voll auszuschöpfen.


Interprozesskommunikation (IPC) ist ein wichtiger Aspekt der parallelen Programmierung, insbesondere wenn es darum geht, Daten zwischen verschiedenen Prozessen auszutauschen oder zu teilen. In Python kann die Interprozesskommunikation durch das `multiprocessing`-Modul ermöglicht werden, das verschiedene Ansätze und Mechanismen für die Kommunikation zwischen Prozessen bietet.

---

# Interprozesskommunikation (IPC)

## Einführung
Das `multiprocessing`-Modul in Python stellt verschiedene Mechanismen für die IPC zur Verfügung, darunter Pipes, Queues und gemeinsam genutzte Speicherobjekte. Diese Werkzeuge ermöglichen es Prozessen, auf sichere und effiziente Weise Informationen auszutauschen.

## Verwendung von Queues
Queues sind wahrscheinlich der einfachste Weg, um Daten zwischen Prozessen auszutauschen. Sie ermöglichen es, Daten in einer FIFO-Reihenfolge (First In, First Out) zu senden und zu empfangen.

### Beispiel: Datenübertragung mit einer Queue
```python
from multiprocessing import Process, Queue

def sender(q):
    q.put("Hallo von Sender!")

def receiver(q):
    msg = q.get()
    print(f"Empfangen: {msg}")

if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=sender, args=(q,))
    p2 = Process(target=receiver, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
```

## Verwendung von Pipes
Pipes bieten eine bidirektionale Kommunikation zwischen zwei Prozessen. Ein Pipe-Objekt hat zwei Enden, jedes Ende wird von einem der kommunizierenden Prozesse verwendet.

### Beispiel: Datenübertragung mit einer Pipe
```python
from multiprocessing import Process, Pipe

def sender(conn):
    conn.send("Hallo von Sender durch Pipe!")
    conn.close()

def receiver(conn):
    msg = conn.recv()
    print(f"Empfangen: {msg}")

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()

    p1 = Process(target=sender, args=(child_conn,))
    p2 = Process(target=receiver, args=(parent_conn,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
```

## Gemeinsam genutzter Speicher
Das `multiprocessing`-Modul stellt auch Möglichkeiten zur Verfügung, um Daten in einem gemeinsam genutzten Speicherbereich zu speichern, auf den von mehreren Prozessen zugegriffen werden kann.

### Beispiel: Verwendung von Value und Array
```python
from multiprocessing import Process, Value, Array

def update_shared(value, array):
    value.value = 3.14159
    for i in range(len(array)):
        array[i] = -array[i]

if __name__ == '__main__':
    shared_value = Value('d', 0.0)
    shared_array = Array('i', range(5))

    print(f'Vorher: {shared_value.value}, {shared_array[:]}')

    p = Process(target=update_shared, args=(shared_value, shared_array))
    p.start()
    p.join()

    print(f'Nachher: {shared_value.value}, {shared_array[:]}')
```

## Zusammenfassung
Die Interprozesskommunikation ist ein wesentlicher Bestandteil der parallelen Programmierung in Python, um Daten zwischen Prozessen zu teilen oder auszutauschen. Das `multiprocessing`-Modul bietet leistungsstarke und flexible Mechanismen für die IPC, einschließlich Queues, Pipes und gemeinsam genutztem Speicher, die eine effiziente Kommunikation zwischen Prozessen ermöglichen.

