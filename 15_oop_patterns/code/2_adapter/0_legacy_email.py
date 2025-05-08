"""
Thema: Adapter Pattern – Realistische Anwendung im E-Mail-Versand

Das Adapter Pattern wird verwendet, um zwei inkompatible Schnittstellen
miteinander zu verbinden. Es kommt oft dann zum Einsatz, wenn bestehender
Code nicht verändert werden soll oder kann – z. B. bei der Integration
älterer Systeme, Bibliotheken oder externer APIs.

In diesem Beispiel:
- Die moderne Anwendung erwartet eine Schnittstelle send_email(to, subject, body).
- Ein älteres Modul stellt aber nur deliver(destination, content_dict) zur Verfügung.
- Der Adapter EmailAdapter passt das alte Interface an das neue an – ohne das alte Modul zu ändern.

Das Adapter Pattern ermöglicht so eine sanfte Migration oder Integration
unterschiedlicher Komponenten mit abweichenden Schnittstellen.
"""


class ModernEmailSender:
    """Neues System nutzt send_email-Methode"""

    def send_email(self, to, subject, body):
        print("modern:", to, subject, body)


class LegacyEmailSender:
    """Alt-System nutzt deliver-Methode"""

    def deliver(self, destination: str, content: dict):
        print(f"[Legacy] Sending to {destination}")
        print(f"Subject: {content['subject']}")
        print(f"Body: {content['body']}")


class EmailClient:
    """Email Client sendet Email an einen Mail-Sender"""

    def __init__(self, email_sender):
        self.email_sender = email_sender

    def send_email(self, to: str, subject: str, body: str):
        self.email_sender.send_email(to, subject, body)


class EmailAdapter:
    """Adapter verbindet Alt- und Neusystem."""

    def __init__(self, email_sender: LegacyEmailSender):
        self.email_sender = email_sender

    def send_email(self, to: str, subject: str, body: str):
        content = {"subject": subject, "body": body}
        self.email_sender.deliver(to, content)


# normale Nutzung (modern)
# client = EmailClient(ModernEmailSender())
# client.send_email("abc@example.com", "hi there!", "ich bins")

# Adapter nutzen (Alt-System)
legacy = LegacyEmailSender()
adapter = EmailAdapter(legacy)
client = EmailClient(adapter)
client.send_email("abc@example.com", "hi there!", "ich bins")
