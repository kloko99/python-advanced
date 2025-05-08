"""
Dieses Modul gibt eine praxisorientierte Einführung in `httpx`,
eine moderne, asynchrone HTTP-Client-Bibliothek für Python 3.7+

`httpx` ist vergleichbar mit `requests`, bietet aber zusätzlich:
- native Unterstützung für `asyncio`
- HTTP/1.1 und HTTP/2 Support
- Timeouts, Streaming, Session-Handling, Redirects, Cookies u.v.m.

Das Modul zeigt synchrone und asynchrone Beispiele, GET/POST-Requests,
Fehlerbehandlung, Header, JSON, Zeitüberschreitungen und parallele Anfragen.

Installation:
    pip install httpx

Geeignet für APIs, Web-Scraping, parallele Datenabfragen usw.
"""

import httpx
import asyncio

# ---------------------------------------------
# Einfacher synchroner GET Request
# ---------------------------------------------
response = httpx.get("https://httpbin.org/get")
print("Status:", response.status_code)
print("JSON:", response.json())


# ---------------------------------------------
# POST Request mit JSON-Daten
# ---------------------------------------------
data = {"name": "Alice", "age": 30}
response = httpx.post("https://httpbin.org/post", json=data)
print("Status:", response.status_code)
print("Gesendet:", response.json()["json"])


# ---------------------------------------------
# Anfrage mit benutzerdefinierten Headern
# ---------------------------------------------
headers = {"Authorization": "Bearer geheim"}
response = httpx.get("https://httpbin.org/headers", headers=headers)
print("Custom Header:", response.json()["headers"])


# ---------------------------------------------
# Zeitüberschreitung behandeln
# ---------------------------------------------
try:
    httpx.get("https://httpbin.org/delay/3", timeout=1.0)
except httpx.ReadTimeout:
    print("Zeitüberschreitung!")


# ---------------------------------------------
# Asynchrone GET-Anfrage (asyncio + httpx)
# ---------------------------------------------
async def fetch():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://httpbin.org/get")
        print("Async Antwort:", response.status_code)


# ---------------------------------------------
# Asynchrone parallele Anfragen
# ---------------------------------------------
async def fetch_parallel():
    urls = ["https://httpbin.org/get?i=" + str(i) for i in range(5)]
    async with httpx.AsyncClient() as client:
        tasks = [client.get(url) for url in urls]
        responses = await asyncio.gather(*tasks)
        for r in responses:
            print(f"{r.url} → {r.status_code}")


if __name__ == "__main__":
    # Starte async Funktionen im Hauptthread
    asyncio.run(fetch())
    asyncio.run(fetch_parallel())
