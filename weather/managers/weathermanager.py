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

        weather_service: WeatherService = WeatherServiceTaMeteo()

        weather_from_service: Weather = WeatherSchema().weather_from_data(weather_service.get_weather_data())

        return weather_from_service
