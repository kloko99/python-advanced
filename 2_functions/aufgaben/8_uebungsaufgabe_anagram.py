"""
1) Anagram (SCHWER)
Schreibe eine Funktion check_anagram(word_1, word_2), die zwei Strings
entgegennimmt und prüft, ob es sich bei diesen Wörtern um ein Anagram handelt.
Groß- und Kleinschreibung soll ignoriert werden.

Als Anagramm wird eine Buchstabenfolge bezeichnet, die aus einer anderen
Buchstabenfolge allein durch Umstellung der Buchstaben gebildet ist, z. B. ist
Erbgut ein Anagramm zu Betrug. Ein Anagramm ist nicht zu verwechseln mit einem
Palindrom, welches eine spezielle Form eines Anagramms darstellt.

Rückgabewert: Boolean

Beispiel:
Leben Nebel

Die zu vergleichenden Wortpaare liegen als Liste von Tupeln vor:
wordlist = [
    ('Leben', 'Nebel'),
    ('Sinn', 'nins'),
    ('auto', 'baum')
]
Rufe check_anagram iterativ für jedes Element von wordlist auf.

Ausgabe:
is anagram Leben Nebel:  True
is anagram Sinn nins:  True
is anagram auto baum:  False


"""
