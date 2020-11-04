# config base file
import os
from littlenv import littlenv
from falcon_caching import Cache

littlenv.load()

WEATHERAPI = {
    'host': os.getenv('WEATHER_HOST'),
    'appid': os.getenv('WEATHER_APP_ID')
}

# cache setup
cache = Cache(
    config=
    {
        'CACHE_EVICTION_STRATEGY': 'time-based',                                               # evicted
        'CACHE_TYPE': 'simple'
    }
)
