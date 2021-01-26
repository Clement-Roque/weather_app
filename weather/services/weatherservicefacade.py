from typing import List, Dict
from weather.services.weatherservice import WeatherService

class WeatherServiceFacade(object):

    def __init__(self) -> None:
        super(WeatherServiceFacade, self).__init__()
        self.weather_services: List[WeatherService] = WeatherService.__subclasses__()  # type: ignore

    def get_weather_data(self) -> Dict[str, int]:

        weather_data: Dict[str, int] = {}

        # TODO :
        # try catch every services call and the global facade get wether behavior with custom weatherewception
        for weather_service_cls in self.weather_services:

            try:
                weather_service: WeatherService = weather_service_cls()  # type: ignore
                weather_data = weather_service.get_weather_data()
                return weather_data
            except Exception:
                pass

        return weather_data
