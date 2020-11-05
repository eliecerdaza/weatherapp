import requests
from config.base import WEATHERAPI

class OpenWeatherService:
    def __init__(self):
        self.config = WEATHERAPI

    def get_by_q(self, query):
        return requests.get(
            url=self.config['host'],
            params={
                "q": query,
                "appid": self.config['appid'],
                "units": 'metric'
            }
        )

    def get_by_location(self, location: list):
        return self._get_by_q(
            query=','.join(location)
        )

    def get_by_days(self, location, days):
        return self._get_by_q(
            query=','.join(location)
        )
