"""
2. Zufallszahl erstellen Schreibe eine Funktion generate_number(), die eine
   Zufallszahl in einem definierten Wertebereich erstellt. generate_number()
   erwartet zwei Parameter: minimum für das Minimum, und maximum für das
   Maximum. Nutze dazu das Modul Random. (LEICHT)

Beispiel
random_number = generate_number(3, 10)
// 8

2.1. Erweitere die Funktion generate_number um einen dritten Parameter
  exclusive. Exclusive ist eine Liste von Werten. Die generierte Zufallszahl
  darf sich nicht in dieser Liste befinden! MITTEL

exclusive = [3, 4, 8]
random_number = generate_number(3, 10, exclusive)
// 7

2.2. Erweitere die Funktion generate_number: falls die Exclusive-Liste so geartet ist, dass sie den kompletten Wertebereich [minimum, maximum] abdeckt, und keine Zufallszahl erzeugt werden kann, soll die Funktion None zurückgeben! MITTEL

exclusive = [3, 4, 5]
random_number = generate_number(3, 5, exclusive)
// None

"""
import random

random.randint(1, 9) # zufallszahl zwischen 1 und 9 erstellen
