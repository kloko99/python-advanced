# Doctest

doctest ist ein Modul, das in der Standardbibliothek der
Programmiersprache Python enthalten ist und die einfache Generierung
 von Tests ermöglicht, die auf der Ausgabe der interaktiven Python Shell basieren, ausgeschnitten und in Docstrings eingefügt werden


    python -m doctest -v example.py

# Python Doctest
wir können in den Docstrings von Funktionen den Shellinput eingeben, 
der von dem Python Modul Doctest ausgewertet werden kann.

## Varianten
wir können Doctest in unseren code importieren und von dort aus starten oder
Doctest mit python -m doctest auf der Commandozeile starten

    python -m doctest stack.py

## Exceptions testen 
wir können auch Exceptions testen. Dazu fügen wir die Ausgabe der Exception
in den Docstring ein (sie 1_beispiel.py)
