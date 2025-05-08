import os
from abc import ABC, abstractmethod


class AbstractApiClient(ABC):

    @abstractmethod
    def get(self): ...


class ApiClient(AbstractApiClient):
    def __init__(self, api_key: str, timeout: int):
        self.api_key = api_key
        self.timeout = timeout

    def get(self, **kwargs):
        return f"called api with key {self.api_key} and get repsonse"


class Service:
    """Api Client wird per Konstruktor-Injection übergeben."""

    def __init__(self, api_client: AbstractApiClient):
        self.api_client = api_client

    def get_daily_data(self):
        return self.api_client.get(type="daily", time_frame=2)


if __name__ == "__main__":

    service = Service(
        ApiClient(
            os.getenv("API_KEY", "xyz"),
            os.getenv("TIMEOUT"),
        )
    )
    result = service.get_daily_data()
    print(result)
