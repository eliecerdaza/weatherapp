# config base file
import os
from littlenv import littlenv
from falcon_caching import Cache

littlenv.load()

WEATHERAPI = {
    'host': os.getenv('WEATHER_HOST'),
    'path': os.getenv('WEATHER_PATH'),
    'forecast': os.getenv('WEATHER_FORECAST_PATH'),
    'appid': os.getenv('WEATHER_APP_ID')
}

# cache setup
cache = Cache(
    config=
    {
        'CACHE_EVICTION_STRATEGY': 'time-based',                                               # evicted
        'CACHE_TYPE': 'simple',
        'CACHE_CONTENT_TYPE_JSON_ONLY': True,
        'CACHE_DEFAULT_TIMEOUT': 120
    }
)
