import requests
from config.base import WEATHERAPI

class OpenWeatherService:
    def __init__(self):
        self.config = WEATHERAPI

    def get_by_city_country(self, query):
        url = f'{self.config["host"]}{self.config["path"]}'
        return requests.get(
            url=url,
            params={
                "q": query,
                "appid": self.config['appid'],
                "units": 'metric'
            }
        )

    def get_forecast(self, lat: float, lon: float):
        url = f'{self.config["host"]}{self.config["forecast"]}'
        return requests.get(
            url=url,
            params={
                "lat": lat,
                "lon": lon,
                "appid": self.config['appid'],
                "units": 'metric',
                "exclude": "hourly,current,minutely,alerts"
            }
        )
