
import requests

CITY_COORDS = {
    "Chennai": (13.0827, 80.2707),
    "Puducherry": (11.9416, 79.8083),
    "Tiruchirappalli": (10.7905, 78.7047),
}


def fetch_weather_bundle(city):
    """Fetch current conditions and a 24-hour model forecast."""
    if city not in CITY_COORDS:
        raise ValueError(f"Unknown city: {city}")

    lat, lon = CITY_COORDS[city]

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": lat,
        "longitude": lon,
        "current": (
            "temperature_2m,relative_humidity_2m,"
            "precipitation,rain,wind_speed_10m"
        ),
        "hourly": (
            "temperature_2m,precipitation_probability,"
            "precipitation,rain"
        ),
        "forecast_hours": 24,
        "timezone": "Asia/Kolkata",
    }

    response = requests.get(url, params=params, timeout=15)
    response.raise_for_status()

    data = response.json()

    if "current" not in data or "hourly" not in data:
        raise ValueError("Weather provider returned incomplete data.")

    return {
        "city": city,
        "current": data["current"],
        "hourly": data["hourly"],
        "units": data.get("hourly_units", {}),
        "timezone": data.get("timezone", "Asia/Kolkata"),
    }


def fetch_weather(city):
    """Backward-compatible current-weather function."""
    return fetch_weather_bundle(city)["current"]
