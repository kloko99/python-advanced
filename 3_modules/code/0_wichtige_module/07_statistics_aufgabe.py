"""
Aufgabe: Datenanalyse mit dem statistics-Modul

Stellen Sie sich vor, Sie arbeiten in einem Unternehmen, das monatlich
die Verkaufszahlen seiner Produkte auswertet. Ihnen liegt folgender
Datensatz mit den Verkaufszahlen (in Tausend) der letzten Monate vor:

    verkaufszahlen = [10, 20, 20, 30, 40, 40, 40, 50, 60]

**Aufgaben:**
1. Berechnen Sie das **arithmetische Mittel** der Verkaufszahlen, um den durchschnittlichen Umsatz zu bestimmen.
2. Ermitteln Sie den **Median**, um den mittleren Verkaufswert zu analysieren.
3. Bestimmen Sie den **Modus**, um das am häufigsten erzielte Verkaufsergebnis herauszufinden.
4. Berechnen Sie die **Standardabweichung**, um die Schwankung der Verkaufszahlen zu bewerten.
5. Berechnen Sie die **Varianz**, um die Streuung der Verkaufszahlen genauer zu analysieren.

**Bonus:**
- Fügen Sie den neuesten Monatswert von **70 Tausend** hinzu und wiederholen Sie alle Berechnungen.
- Analysieren Sie, wie sich der neue Wert auf die Kennzahlen auswirkt.
"""

# Importiere das statistics-Modul für statistische Berechnungen
import statistics

# Beispiel-Datensatz: Verkaufszahlen in Tausend
verkaufszahlen = [10, 20, 20, 30, 40, 40, 40, 50, 60]
