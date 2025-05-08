"""
Einsatz von else an einem konkreten Beispiel
"""
import requests


def get_temperature(latitude: float, longitude: float) -> float:
    """Hole Temperatur für einen Ort definiert duch Längen- und Breitengrad."""
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}&longitude={longitude}"
        "&hourly=temperature_2m"
    )
    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()  # falls zb. 400 Server, Exception auslösen
    except requests.exceptions.RequestException as e:
        print(f"API ERROR: {e}")
    else:
        data = response.json()
        return data["hourly"]["temperature_2m"][0]



wetter = get_temperature(latitude=52.52, longitude=13.41)
# wetter = get_temperature(latitude=0, longitude=13.41)  # Wetter Äquator
print("Wetter:", wetter)
