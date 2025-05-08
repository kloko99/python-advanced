"""
Dieses Modul gibt eine Einführung in Playwright für Python,
ein modernes Tool zur Steuerung von Webbrowsern über eine API.

Playwright erlaubt automatisierte Browser-Interaktion wie z. B.:
- Webseiten aufrufen und DOM-Elemente lesen
- Formulare ausfüllen, Buttons klicken
- Screenshots machen, Inhalte extrahieren
- JavaScript-Seiten vollständig laden

Playwright unterstützt Chromium, Firefox und WebKit, auch im
headless (unsichtbaren) Modus und mit async-API.

Installation:
    pip install playwright
    playwright install

Dieses Beispiel zeigt ein einfaches Browsing und DOM-Interaktion.
"""

import asyncio
from playwright.async_api import async_playwright

URL = "https://friendlybytes.net"


async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(URL)

        # Titel und Screenshot
        title = await page.title()
        print("Seitentitel:", title)

        await page.screenshot(path="screenshot.png")
        print("Screenshot gespeichert.")

        # Text extrahieren
        content = await page.inner_text("h1")
        print("H1-Überschrift:", content)

        await browser.close()


if __name__ == "__main__":
    asyncio.run(run())
