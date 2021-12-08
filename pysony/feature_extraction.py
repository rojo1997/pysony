from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import reverse_geocoder as rg
import requests

class ReverseGeocoder(BaseEstimator, TransformerMixin):
    """Reverse geocoder feature coordinate extraction
        Coordinate specification <lon,lat>
    """
    columns = ["name","admin1","admin2"]
    def __init__(self, mode: int = 1):
        """Reverse geocoder feature coordinate extraction

        Args:
            mode (int, optional): Mode 1: Single-threaded K-D Tree. Mode 2: Multi-threaded K-D Tree. Defaults to 1.
        """
        self.mode = mode

    def fit(self, X, y):
        return self

    def transform(self, X: np.ndarray, y: np.ndarray = None):
        """Reverse geocoder feature coordinate extraction

        Args:
            X (np.ndarray): coordinate matrix <lon,lat>
            y (np.ndarray, optional): Defaults to None.

        Returns:
            [numpy.ndarray]: matrix specification <name,admin1,admin2>
        """
        result = rg.search(
            geo_coords = [(x[1],x[0]) for x in X],
            mode = self.mode
        )
        return np.array([
            [r["name"],r["admin1"],r["admin2"]]
        for r in result])

class OpenWeatherMap(BaseEstimator, TransformerMixin):
    """Open Weather Map feature coordinate extraction
        Coordinate specification <lon,lat>
    """
    columns = [
        "temp",
        "feels_like",
        "temp_min",
        "temp_max",
        "pressure",
        "humidity",
        "wind_deg",
        "wind_speed"
    ]
    def __init__(self, appid: str):
        """Reverse geocoder feature coordinate extraction

        Args:
            appid (str, optional): apikey
        """
        self.appid = appid
        self.url = "http://api.openweathermap.org/data/2.5/weather"

    def fit(self, X, y):
        return self
    
    def transform(self, X: np.ndarray, y: np.ndarray = None):
        """Open Weather Map feature coordinate extraction

        Args:
            X (np.ndarray): coordinate matrix <lon,lat>
            y (np.ndarray, optional): Defaults to None.

        Returns:
            [numpy.ndarray]: matrix specification <
                temp,
                feels_like,
                temp_min,
                temp_max,
                pressure,
                humidity,
                wind_deg,
                wind_speed
            >
        """
        result = []
        for x in X:
            result_query = requests.get(
                url = self.url,
                params = {
                    "lon": x[0],
                    "lat": x[1],
                    "appid": self.appid
                }
            )
            if result_query.status_code == 200:
                result_json = result_query.json()
                result.append({
                    "temp": result_json["main"]["temp"],
                    "feels_like": result_json["main"]["feels_like"],
                    "temp_min": result_json["main"]["temp_min"],
                    "temp_max": result_json["main"]["temp_max"],
                    "pressure": result_json["main"]["pressure"],
                    "humidity": result_json["main"]["humidity"],
                    "wind_deg": result_json["wind"]["deg"],
                    "wind_speed": result_json["wind"]["speed"],
                })
        return np.array([list(r.values()) for r in result])