import logging
import datetime
import json
import falcon
from app.services import OpenWeatherService
from app.adapter import WeatherAdapter
from config import cache


class WeatherView:

    def on_get(self, req, resp):
        city = req.get_param('city') or ''
        country = req.get_param('country') or ''
        day = req.get_param('day') or '-1'
        try:
            weather_service = OpenWeatherService()
            weather_response = self._get_weather(weather_service, city, country)
            weather_data = weather_response.json()
            if day != '-1':
                coord = weather_data.get('coord')
                weather_data["forecast"] = self._get_forecast(weather_service, coord, int(day))
            weather_adapter = WeatherAdapter()
            resp.status = falcon.HTTP_200
            resp.content_type = 'application/json'
            resp.body = json.dumps(
                weather_adapter.parse_weather(weather_data)
            )
        except Exception as e:
            logging.error(e)
            resp.status = falcon.HTTP_500
            resp.content_type = 'application/json'
            resp.body = 'Error on weather request'

    def _get_weather(self, ws, city, country):
        if cache.get(f'{city}_{country}'):
            return cache.get(f'{city}_{country}')
        weather_response = ws.get_by_city_country(f'{city},{country}')
        cache.set(f'{city}_{country}', weather_response)
        return weather_response

    def _get_forecast(self, ws, coord:dict, day:int) -> dict:
        if cache.get(f'{coord["lat"]}_{coord["lon"]}_{day}'):
            return cache.get(f'{coord["lat"]}_{coord["lon"]}_{day}')
        forecast_response = ws.get_forecast(coord['lat'], coord['lon'])
        forecast_data = forecast_response.json()
        forecast = forecast_data.get('daily')[day%7]
        now = datetime.datetime.now()
        forecast["requested_time"] = now.strftime("%Y-%m-%d %H:%M:%S")
        cache.set(f'{coord["lat"]}_{coord["lon"]}_{day}', forecast)
        return forecast
