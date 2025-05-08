"""
Dieses Modul zeigt eine Einführung in das Python-Modul `typer`,
das den Bau moderner Kommandozeilen-Interfaces (CLI) vereinfacht.

`typer` basiert auf `click`, nutzt aber vollständige Type Hints,
um automatisch Dokumentation, Hilfe, Parameter-Validierung
und Autovervollständigung zu generieren.

Installation:
    pip install typer[all]

Vorteile:
- Deklarativer Stil mit Python-Funktionen
- Typisierte Argumente + automatische Konvertierung
- Einfache Doku + Hilfetexte
- Unterstützt Unterkommandos (Subcommands)

Dieses Beispiel zeigt einfache Befehle mit Argumenten und Optionen.

Nutzung:
    python 2_typer.py hallo Klaus
    python 2_typer.py addiere 99 --b 3 (b ist hier optional)
    python 2_typer.py subtrahiere 99 3

"""

import typer

app = typer.Typer()

# Einfacher Befehl mit Argument


def hallo(name: str):
    """Grüßt den Benutzer."""
    typer.echo(f"Hallo, {name}!")


app.command()(hallo)


# Kommando mit Option (optional, mit Default-Wert)
@app.command()
def addiere(a: int, b: int = typer.Option(1, help="Zahl zum Addieren")):
    """Addiert zwei Zahlen."""
    result = a + b
    typer.echo(f"Ergebnis: {result}")


@app.command()
def subtrahiere(a: int, b: int):
    """Subtrahiert zwei Zahlen."""
    result = a - b
    typer.echo(f"Ergebnis: {result}")


# Kommando mit Flag (boolesche Option)
@app.command()
def status(verbose: bool = typer.Option(False, "--verbose", "-v")):
    """Zeigt den aktuellen Status an."""
    if verbose:
        typer.echo("Status: OK (detailliert)")
    else:
        typer.echo("Status: OK")


if __name__ == "__main__":
    app()  # CLI starten
