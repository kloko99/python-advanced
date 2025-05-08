# Flood Fill Algorithmus – Konzept & Erklärung

Der **Flood Fill Algorithmus** ist ein Verfahren zur **Flächenfüllung**, ähnlich wie das Farbeimer-Werkzeug in Malprogrammen:  
Er ersetzt alle angrenzenden Zellen gleicher Farbe, beginnend bei einem Startpunkt.

---

## Idee

Gegeben ist ein zweidimensionales Gitter (z. B. ein Bild). Du klickst auf ein Feld – alle **zusammenhängenden** Felder derselben Farbe werden in eine neue Farbe geändert.

---

### Typische Anwendung

- Füllen von Bereichen in Bildbearbeitungen  
- Zählen zusammenhängender Flächen in Grid-Problemen  
- Labyrinthe, Kartenspiele, Gebietsberechnungen

---

## Ablauf (rekursiv)

**Eingabe:**
- Startkoordinaten `(x, y)`
- Ziel-Farbe `target`
- Ersatz-Farbe `replacement`

**Schritte:**

1. Prüfe: Ist `(x, y)` innerhalb der Grenzen?
2. Hat das Feld die *Ziel-Farbe*?
3. Falls ja:  
   - Färbe es um
   - Rufe Flood Fill für die **4 Nachbarn** auf (oben, unten, links, rechts)

---

### Visualisierung

Angenommen, wir haben dieses Grid (Zahlen = Farben):

```
1 1 2 2
1 2 2 2
1 1 2 2
```

Start bei `(0,0)`, Farbe `1` → neue Farbe `9`:

```
1 1 . .
1 . . .
1 1 . .
```

Flood Fill ersetzt alle `1` durch `9`:

```
9 9 2 2
9 2 2 2
9 9 2 2
```

---

## Komplexität

- **Zeit:** O(N) – alle Zellen können im Worst Case besucht werden  
- **Platz (rekursiv):** O(N) – durch den Call Stack

---

## Varianten

- **4-Richtungen:** nur oben/unten/links/rechts  
- **8-Richtungen:** zusätzlich diagonale Nachbarn  
- **Iterativ:** mit eigener Stack- oder Queue-Struktur (um Rekursionstiefe zu vermeiden)

---

## Wichtig

- Rekursive Lösung kann bei großen Feldern zum **Stack Overflow** führen  
- Iterative Lösung (mit Queue oder Stack) ist robuster

