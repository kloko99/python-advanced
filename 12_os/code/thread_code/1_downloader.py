"""
Das Programm lädt "parallel" Webseiten runter,
und das soll einmal ohne Threading und einmal mit Threading
gemacht werden.

"""

import requests
import threading
import time
from pathlib import Path
from typing import Callable
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse
from queue import Queue

DATA_DIR = Path(__file__).parent / "data"


URLS = [
    "https://www.google.com/",
    "https://www.facebook.com/",
    "https://www.amazon.com/",
    "https://www.youtube.com/",
    "https://www.wikipedia.org/",
    "https://www.twitter.com/",
    "https://www.instagram.com/",
    "https://www.netflix.com/",
    "https://www.linkedin.com/",
    "https://www.reddit.com/",
    "https://www.apple.com/",
    "https://www.microsoft.com/",
    "https://www.yahoo.com/",
    "https://www.twitch.tv/",
    "https://www.github.com/",
    "https://www.stackoverflow.com/",
    "https://www.quora.com/",
    "https://www.medium.com/",
    "https://www.nytimes.com/",
    "https://www.wikipedia.org/",
]


def create_data_dir(path: Path) -> None:
    """Create data directory in current folder."""
    if not Path.is_dir(path):
        Path.mkdir(path)


def delete_files(path: Path) -> None:
    """Delete all files in dir."""
    if not Path.is_dir(path):
        raise ValueError("Dieser Pfad existiert nicht.")

    for file_name in Path.iterdir(path):
        file = path / file_name
        if Path.is_file(file):
            file.unlink()


def save_data_as_file(data: str, file_name: str) -> None:
    """Save HTML-Data in data-Directory."""
    with open(DATA_DIR / file_name, mode="w", encoding="utf-8") as f:
        f.write(data)


def download_page(url: str, q: Queue = None) -> str:
    """Quellcode einer Webseite runterladen und speichern."""

    # Um Daten zwischen Threads auszutauschen, dient die thraed-safe Queue als
    # geeignete Datenstruktur
    if q is not None:
        q.put(f"Downloaded: {url}")

    page = requests.get(url)
    # falls ein fehler im Thread auftritt, am besten im Thread selber abfangen
    # raise ValueError("hier gibts nen fehler")

    file_name = str(hash(url)) + ".html"
    save_data_as_file(page.text, file_name)
    return f"Downloaded: {url}"


def classic_downloader() -> None:
    """Download all urls synchronized."""
    for url in URLS:
        download_page(url)


def threaded_downloader() -> None:
    """Download all urls in threaded manner."""
    q = Queue()  # Zum Datenaustausch zwischen den Threads
    threads = []
    for url in URLS:
        # Thread starten
        thread = threading.Thread(target=download_page, args=(url, q))
        thread.start()
        threads.append(thread)

    [t.join() for t in threads]  # Wir warten hier auf das Beendender Threads

    # Die Queue, in die die Threads geschrieben haben, ausgeben.
    while not q.empty():
        print("=> ", q.get())


def modern_threaded_downloader() -> None:
    """der Threadpool Executor startet Threads komfortabel"""
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(download_page, url) for url in URLS]

        # die fertigen Threads (Futures) ausgeben
        for future in as_completed(futures):
            print("=>", future.result())


def super_modern_threaded_downloader() -> None:
    """die map-Methode des Executors vereinfacht das ganze noch mehr."""
    with ThreadPoolExecutor() as executor:
        results = executor.map(download_page, URLS)
        for result in results:
            print(result)


def download(downloader: Callable) -> None:
    delete_files(DATA_DIR)
    start = time.perf_counter()
    downloader()
    end = time.perf_counter()
    print(f"Der Download hat {end - start: .2f} Sekunden gedauert.")


if __name__ == "__main__":
    create_data_dir(DATA_DIR)
    # download(downloader=classic_downloader)
    download(downloader=threaded_downloader)
    # download(downloader=modern_threaded_downloader)
    # download(downloader=super_modern_threaded_downloader)
