r"""
Thema: Reguläre Ausdrücke (Regex) in Python

Dieses Skript vermittelt grundlegende und fortgeschrittene Konzepte
zur Nutzung von regulären Ausdrücken mit dem Modul `re`. Es deckt
Metazeichen, Quantoren, Gruppen, Anker, Identifizierer und Ersetzungen ab.

Nützliche Ressourcen:
https://cheatography.com/davechild/cheat-sheets/regular-expressions/pdf/
https://regex101.com/


 QUANTOREN
 ? => entweder null oder ein Zeichen
 * => entweder null oder unbegrenzt
 + => entweder 1 oder mehr
 {n} oder {n,} oder {min,max} => entweder n-zeichen oder ab n zeichen oder # min-max-Bereich

 ANCHORS
 ^ => am Anfang eines Strings
 $ => am Ende eines String
 \b => Am Anfang oder Ende eines Wortes (\B => not boundary)

 IDENTIFYER
. => irgendein Zeichen
[a-z0-9] => alle Zeichen von a - z und 0 - 9
[abc] => Menge der erlaubten Zeichen
\d => Zahl 0-9, \D=> Nicht Zahl
\w => Word a-z A-Z 0-9, \W => nicht-Wort
\s => Whitespace, \S => not-Whitespace
(ab) => Gruppe
"""

import re

# Wozu Regex? Alley Maier finden...
alle_maier = "Meyer Mauser Maier Mayer Wolf Meier Meir Major Mayr Majer"

# Verfeinerung mit Quantor {1}: mindestens ein bestimmter Buchstabe
alle_maier = "Meyer Meyyer Maiier Mayer Meier Meir Mai Major"

# Literale erkennen: "om" kommt exakt so im Text vor
m = "omikron_omikron-omaha-Gelber_tagesstern_2_7"

# Quantoren ? * + und {n,m} im Einsatz

# Zeichenklassen: [] für einzelne erlaubte Buchstaben

# Quantoren kombiniert: suche nach 'omi' gefolgt von einem oder mehreren 'i'

# .*? = möglichst kurze (nicht-gierige) Erkennung bis zu einem Zielwort

# Kombination: beginnt mit 'om', endet mit 'n', dazwischen beliebige Kleinbuchstaben

# \d steht für Ziffern, \w für Wortzeichen, \s für Leerzeichen

# Beispiele für Anker: ^ (Anfang), $ (Ende), \b (Wortgrenze)

# Aufgabe: Extrahiere Wörter, die mit 'x' beginnen und mit drei Ziffern enden
m2 = "Klara Zelebral xKryptomat Periklor 876"

# Suche nach Telefonnummern-Mustern
tel = "telnrs0049-89-234, 0049-78-203 +49-23-9290"

# Aufgabe: Extrahiere zwei- oder dreistellige Zahlen
zahlen = "19 -23 xxxx 98 230 ----328"

# Wörter mit genau drei Wortzeichen (\w) extrahieren

# Aufgabe: Wörter, die mit S oder B beginnen
namen = "Brunn Romilda Tomy Sylvestr Kassandra Wohmbe Sendr Signar"

# Aufgabe: Namen, die mit S oder B beginnen und mit 'r' enden

# Begrenzte Wiederholungen {2,4} mit und ohne ? (greedy / non-greedy)
pfeile = "<<<<>><<<<>>>"

# Negative Lookahead: String enthält nicht "ab"
test = "zaabrakadabra"

# Gruppierungen: () für Erfassungen, (?:) für nicht-erfassende Gruppen

# Gruppierung mit + (mind. 1x) und * (beliebig oft)

# Alternative mit (London|Paris|Strasbourg)
m = "The destination is London!"

# Aufgabe: Finde was nach "Gelber_" bis vor Zahl steht
stern = "omikron_omikron-omaha-Gelber_Feuerstern_23_87"

# Aufgabe: Finde zweistellige Zahlen, vor denen Leerzeichen oder "-" steht
zahlen2 = "xx 19 -23 xxxx 98 230 78 ----328"

# Zahlen zwischen festen Buchstaben extrahieren
m = "AAA3230BBB2302AAA"

# Ersetzen mit re.sub: Wörter durch "__" ersetzen, die mit s oder l anfangen
# und mit e enden. Nutze dazu das Word-Boundary (\b)
text = (
    "If you can't take a little bloody nose, maybe you oughtta go home and"
    "crawl under your bed. It's not safe out here. It's wondrous, treasures to"
    "satiate desires both subtle and gross; but it's not for the timid."
)
