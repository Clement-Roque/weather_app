from weather.models.weather import Weather
from weather.services.weatherservicefacade import WeatherServiceFacade
from weather.schemas.weatherschema import WeatherSchema

class WeatherManager(object):

    def __init__(self) -> None:
        super(WeatherManager, self).__init__()

    def get_current_weather(self) -> Weather:

        weather_service: WeatherServiceFacade = WeatherServiceFacade()

        weather_from_service: Weather = WeatherSchema().weather_from_data(weather_service.get_weather_data())

        return weather_from_service
