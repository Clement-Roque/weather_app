import json
from weather.models.weather import Weather
from weather.services.weatherservicetameteo import WeatherServiceTaMeteo
from weather.services.weatherservice import WeatherService
from weather.schemas.weatherschema import WeatherSchema

class WeatherManager(object):

    def __init__(self) -> None:
        super(WeatherManager, self).__init__()

    def get_current_weather(self) -> Weather:

        # TODO :
        # Encapsulate the weather service choice into a dedicated element
        # Service must return a weather dict, so
        weather_service: WeatherService = WeatherServiceTaMeteo()
        temperature: int = weather_service.get_temperature()

        raw_weather: str = json.dumps({"temperature": temperature})

        weather_from_json: Weather = WeatherSchema().weather_from_json(raw_weather)

        return weather_from_json
