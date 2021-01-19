import json
from weather.models.weather import Weather
from weather.services.weatherservicetameteo import WeatherServiceTaMeteo
from weather.services.weatherservice import WeatherService
from weather.schemas.weatherschema import WeatherSchema

class WeatherManager(object):

    def __init__(self) -> None:
        super(WeatherManager, self).__init__()

    def get_current_weather(self) -> Weather:

        weather_service: WeatherService = WeatherServiceTaMeteo()

        temperature: int = weather_service.get_temperature()

        raw_weather: str = json.dumps({"temperature": temperature})
        weather_schema: WeatherSchema = WeatherSchema()
        weather_from_json: Weather = weather_schema.loads(raw_weather)

        return weather_from_json

