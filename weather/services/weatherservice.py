from typing import Dict
import abc

class WeatherService(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_temperature(self) -> int:
        pass

    @abc.abstractmethod
    def get_weather_data(self) -> Dict[str, int]:
        pass
