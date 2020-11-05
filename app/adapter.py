import datetime

class WeatherAdapter:

    def parse_weather(self, weather: dict) -> dict:
        city = weather.get('name') or ''
        country = weather.get('sys', {}).get('country') or ''
        humidity = weather.get('main', {}).get('humidity')
        sunrise = weather.get('sys', {}).get('sunrise')
        sunset = weather.get('sys', {}).get('sunset')
        response = {
            "location_name": f'{city}, {country}',
            "temperature": self.temperature(weather),
            "wind": self.wind(weather),
            "cloudiness": weather.get('clouds', {}).get('all'), # TODO translate this
            "pressure": self.pressure(weather),
            "humidity": f"{humidity}%",
            "sunrise": self.sunx(sunrise),
            "sunset": self.sunx(sunset),
            "geo_coordinates": self.geo_coordinates(weather),
            "requested_time": datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        }
        return response

    def temperature(self, temperature:float) -> str:
        temp = weather.get('main', {}).get('temp')
        return f'{temp} ˚C'

    def wind(self, data: dict) -> str:
        wind = data.get('wind')
        speed = wind["speed"] # TODO translate this
        direction = wind["deg"] # TODO translate this
        return f'Gentle breeze, {speed} m/s, west-northwest'

    def pressure(self, weather: dict) -> str:
        pressure = weather.get('main', {}).get('pressure')
        return f'{pressure} hda'

    def sunx(self, sunrise: int) -> str:
        sunrise = datetime.datetime.fromtimestamp(sunrise)
        return sunrise.strftime('%H:%M')

    def geo_coordinates(self, data:dict) -> str:
        lat = data.get('coord', {}).get('lat')
        lon = data.get('coord', {}).get('lon')
        return f'[{lat}, {lon}]'