# Zahlenratespiel
# Zufallszahl errechnen (mit random.randint), zb. 4
# maximale Rateversuche: 4
# whileloop
# pro Loop ein User Input. Ist user input nicht gleich der Zufallszahl
# leider falsch, bitte nochmal raten
# im Glück gehabt, du hast gewonnen!
# falls die Anzahl der Rateversuche >= der maximalen Rateversuche, Game over

import random

MAX_ATTEMPS = 3
MIN = 1
MAX = 6

# Zufallszahl ziehen
number = random.randint(MIN, MAX)


# Solange loopen, solange die Versuche kleiner als
# MAX_ATTEMPS sind
