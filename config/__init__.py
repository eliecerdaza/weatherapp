import falcon
from falcon_caching import Cache
from spectree import SpecTree
from config.base import cache
from app.views import WeatherViews

app = falcon.API(middleware=cache.middleware)

api = SpecTree(
    'falcon',
    title='Weather App',
    version='v1.0',
    path='docs'
)

app.add_route(
    '/weather',
    WeatherViews()
)
