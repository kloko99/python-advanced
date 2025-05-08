# 🔍 Rekursive Binärsuche – Schritt für Schritt erklärt

Die **Binärsuche** ist ein effizienter Algorithmus zum Auffinden eines bestimmten Werts in einer **aufsteigend sortierten Liste**. Der rekursive Ansatz folgt einem klaren Prinzip: *Teile und herrsche*.

---

## 🧠 Funktionsweise

Statt jeden Eintrag der Liste nacheinander zu prüfen (wie bei der linearen Suche), wird bei der Binärsuche die Liste **immer wieder halbiert**, bis das gesuchte Element gefunden ist – oder als nicht vorhanden erkannt wird.

---

### 🔄 Rekursiver Ablauf

Gegeben ist eine sortierte Liste wie:

```
[ 5, 8, 15, 23, 42, 60, 77 ]
```

Wir suchen die Zahl `42`. Die Binärsuche funktioniert so:

1. **Start:**  
   Nimm das mittlere Element der Liste → hier: `23`  
   → `23 < 42`, also muss `42` **rechts** davon liegen.

2. **Neue Liste:**  
   Betrachte nur den rechten Teil:  
   ```
   [ 42, 60, 77 ]
   ```

3. **Wieder Mitte wählen:**  
   Mitte ist `60`. → `60 > 42`, also liegt `42` **links** davon.

4. **Neue Liste:**  
   Nur noch ein Element: `[42]`  
   → Treffer!

---

### 📊 Visualisierung

```
Suche 42 in: [5, 8, 15, 23, 42, 60, 77]
                        ↑
                      Mitte = 23

→ 42 > 23 → rechts suchen

[42, 60, 77]
 ↑
Mitte = 60

→ 42 < 60 → links suchen

[42]
 ↑
Mitte = 42 → Treffer!
```

---

## ⏱️ Komplexität

- **Best Case:** Treffer bei erstem Vergleich → **O(1)**
- **Average/Worst Case:** Liste wird bei jedem Schritt halbiert → **O(log n)**

---

## ⚠️ Bedingungen

- Die Liste **muss sortiert** sein.  
  Sonst funktioniert die Strategie des "Hälfte-Wegwerfens" nicht.

- Der rekursive Algorithmus benötigt **zusätzlichen Speicher** (Stack), da jeder Funktionsaufruf sich selbst wieder aufruft.

---

## ✅ Vorteile

- Sehr effizient bei großen, sortierten Datenmengen  
- Klarer und eleganter Algorithmus  
- Einfach in rekursive Denkweise übertragbar

