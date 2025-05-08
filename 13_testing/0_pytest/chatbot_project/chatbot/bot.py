import requests


class Chatbot:
    def __init__(self, name: str = "Bot"):
        self.name: str = name
        self.history: str = []

    def greet(self) -> str:
        return f"Hallo! Ich bin {self.name}. Wie kann ich helfen?"

    def ask_api(self, message: str) -> str:
        """Fragt eine API und gibt die Antwort zurück."""
        response = requests.get("https://example.com")
        if response.status_code == 200:
            return f"Antwort empfangen für '{message}'"
        else:
            return f"Fehler: Antwortcode {response.status_code}"

    def remember(self, message: str) -> None:
        """Speichert eine Nachricht im Verlauf."""
        self.history.append(message)

    def has_seen(self, keyword: str) -> bool:
        """Prüft, ob ein Wort schon im Verlauf vorkam."""
        return any(keyword.lower() in msg.lower() for msg in self.history)

    def respond_length_hint(self, message: str) -> str:
        """Antwortet, ob die Nachricht kurz oder lang ist."""
        word_count = len(message.strip().split())
        if word_count < 3:
            return "Bitte etwas ausführlicher."
        return "Danke für die ausführliche Nachricht."

    def get_from_history(self, index: str) -> str:
        """Gibt eine Nachricht aus dem Verlauf zurück oder wirft IndexError."""
        if index < 0 or index >= len(self.history):
            raise IndexError("Ungültiger Index im Chatverlauf.")
        return self.history[index]
