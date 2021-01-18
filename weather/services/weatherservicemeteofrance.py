from weather.services.weatherservice import WeatherService

class WeatherServiceMeteoFrance(WeatherService):

    def __init__(self) -> None:
        super(WeatherService, self).__init__()
        self.url = "https://meteofrance.com/previsions-meteo-france/montpellier/34000"
