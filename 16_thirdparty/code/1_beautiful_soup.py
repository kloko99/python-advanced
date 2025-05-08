"""
Dieses Modul gibt eine Einführung in die Bibliothek BeautifulSoup,
die zum Parsen und Analysieren von HTML und XML in Python verwendet wird.

BeautifulSoup ist besonders hilfreich beim Web Scraping, um gezielt
Inhalte aus Webseiten zu extrahieren – z. B. Überschriften, Links,
Tabelleninhalte oder spezifische Tags mit Attributen.

Installation:
    pip install beautifulsoup4 lxml

In Kombination mit Bibliotheken wie `requests` oder `httpx` lässt
sich damit strukturiert auf HTML-Daten zugreifen und diese verarbeiten.

Die folgenden Beispiele zeigen das Parsen von HTML-Strings, das Navigieren
im Baum und die Suche nach Tags, Klassen, Attributen oder Texten.
"""

from bs4 import BeautifulSoup
import httpx

# ---------------------------------------------
# Einfaches HTML parsen
# ---------------------------------------------
html = """
<html>
  <head><title>Beispielseite</title></head>
  <body>
    <h1>Willkommen</h1>
    <p class="info">Dies ist ein <b>Beispiel</b>-Text.</p>
    <a href="https://example.com">Mehr Infos</a>
  </body>
</html>
"""

soup = BeautifulSoup(html, "lxml")

# ---------------------------------------------
# Zugriff auf einzelne Tags
# ---------------------------------------------
print("Titel:", soup.title.text)
print("H1:", soup.h1.string)
print("Link (href):", soup.a["href"])

# ---------------------------------------------
# Suche nach Tags mit bestimmter Klasse
# ---------------------------------------------
p_info = soup.find("p", class_="info")
print("Absatz mit Klasse 'info':", p_info.text)

# ---------------------------------------------
# Alle Links ausgeben
# ---------------------------------------------
for link in soup.find_all("a"):
    print("Link gefunden:", link.get("href"))

# ---------------------------------------------
# Tag-Inhalte ändern (Beispielmanipulation)
# ---------------------------------------------
soup.h1.string = "Hallo Welt!"
print("Verändertes H1:", soup.h1)

# ---------------------------------------------
# Neue Elemente einfügen
# ---------------------------------------------
neues_tag = soup.new_tag("p")
neues_tag.string = "Dies ist ein neuer Absatz."
soup.body.append(neues_tag)
print("HTML nach Hinzufügen:")
print(soup.prettify())

# ---------------------------------------------
# Web Scraping-Beispiel mit httpx + BeautifulSoup
# ---------------------------------------------
url = "https://httpbin.org/html"  # Beispielseite mit HTML-Inhalt
response = httpx.get(url)

if response.status_code == 200:
    soup_live = BeautifulSoup(response.text, "lxml")
    title = soup_live.find("h1")
    print("Titel auf externer Seite:", title.text if title else "kein <h1> gefunden")
else:
    print("Fehler beim Abruf der Seite:", response.status_code)
