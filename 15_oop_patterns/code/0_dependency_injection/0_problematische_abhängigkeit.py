"""
In diesem Beispiel haben wir zwei Probleme:
- Abhängigkeit von Keys
- Abhängigkeit von ApiClient im Service
"""

import os


class ApiClient:
    def __init__(self):
        self.api_key = os.getenv("API_KEY")  # << Abhängigkeit
        self.timeout = os.getenv("TIMEOUT")  # << Abhängigkeit

    def get(self, **kwargs):
        return "called api and get repsonse"


class Service:
    """Service nutzt den API Client um daily daten zu holen."""

    def __init__(self):
        self.api_client = ApiClient()  # << Abhängigkeit

    def get_daily_data(self):
        return self.api_client.get(type="daily", time_frame=2)


if __name__ == "__main__":
    service = Service()
    result = service.get_daily_data()
    print(result)
