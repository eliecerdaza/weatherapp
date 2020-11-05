import json
import falcon
from app.services import OpenWeatherService
from app.adapter import WeatherAdapter
from config import cache

@cache.cached(timeout=120)
class WeatherViews:

    def on_get(self, req, resp):
        city = req.get_param('city') or ''
        country = req.get_param('country') or ''
        weather_service = OpenWeatherService()
        weather_response = weather_service.get_by_q(f'{city},{country}')
        weather_adapter = WeatherAdapter()
        resp.status = falcon.HTTP_200
        resp.content_type = 'application/json'
        resp.body = json.dumps(
            weather_adapter.parse_weather(weather_response.json())
        )
