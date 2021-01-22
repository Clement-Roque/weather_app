from typing import List, Dict
from weather.services.weatherservice import WeatherService
# from weather import services


class WeatherServiceFacade(object):

    def __init__(self) -> None:
        super(WeatherServiceFacade, self).__init__()
        self.weather_services: List[WeatherService] = [
            weather_service_cls for weather_service_cls in WeatherService.__subclasses__()]

    def get_weather_data(self) -> Dict[str, int]:

        weather_data: Dict[str, int] = {}

        # TODO :
        # try catch every services call and the global facade get wether behavior with custom weatherewception
        for weather_service_cls in self.weather_services:

            weather_service: WeatherService = weather_service_cls()
            weather_data = weather_service.get_weather_data()
            return weather_data

        return weather_data
