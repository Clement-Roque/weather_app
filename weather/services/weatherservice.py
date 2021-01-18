import abc

class WeatherService(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_temperature(self) -> int:
        pass
