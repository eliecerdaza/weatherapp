from unittest.mock import Mock, patch
import pytest
from falcon import testing
from config import app
from app.views import WeatherView


@pytest.fixture
def client():
    return testing.TestClient(app)

def test_weather_response(client):
    weather = {
        "location_name": "Bogotá, CO",
        "temperature": "9 ˚C",
        "wind": "Gentle breeze, 1 m/s, west-northwest",
        "cloudiness": 40,
        "pressure": "1026 hda",
        "humidity": "93%",
        "sunrise": "05:41",
        "sunset": "17:38",
        "geo_coordinates": "[4.61, -74.08]",
        "requested_time": "2020-11-05 23:01:18"
    }
    params = {
        "city": "Bogota",
        "country": "co"
    }
    response = client.simulate_get('/weather', params=params)
    assert response.status_code == 200, 'status 200'
    assert response.json.keys() == weather.keys(), 'correct weather keys'
    response_2 = client.simulate_get('/weather', params=params)
    assert response_2.json['requested_time'] == response.json.get('requested_time'), 'cache works'

def test_forecast(client):
    forecast = {
        "location_name":"Bogotá, CO",
        "temperature":"9 ˚C",
        "wind":"Gentle breeze, 1 m/s, west-northwest",
        "cloudiness":40,
        "pressure":"1026 hda",
        "humidity":"93%",
        "sunrise":"05:41",
        "sunset":"17:38",
        "geo_coordinates":"[4.61, -74.08]",
        "requested_time":"2020-11-05 23:01:18",
        "forecast":{
            "dt":1604592000,
            "sunrise":1604572903,
            "sunset":1604615888,
            "temp":{
                "day":17.68,
                "min":9,
                "max":17.68,
                "night":9,
                "eve":15.42,
                "morn":10.5
            },
            "feels_like":{
                "day":17.47,
                "night":8.28,
                "eve":15.71,
                "morn":10.07
            },
            "pressure":1015,
            "humidity":67,
            "dew_point":11.66,
            "wind_speed":0.96,
            "wind_deg":258,
            "weather":[
                {
                    "id":501,
                    "main":"Rain",
                    "description":"moderate rain",
                    "icon":"10d"
                }
            ],
            "clouds":69,
            "pop":0.96,
            "rain":10.97,
            "uvi":14.4
        }
    }
    params = {
        "city": "Bogota",
        "country": "co",
        "day": 1
    }
    response = client.simulate_get('/weather', params=params)
    assert response.status_code == 200, 'status 200'
    assert response.json['forecast'].keys() == forecast['forecast'].keys(), 'correct forecast keys'
