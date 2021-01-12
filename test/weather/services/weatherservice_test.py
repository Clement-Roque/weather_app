from weather.services.weatherservice import WeatherService

class TestWeatherService(object):

    def test_weather_service(self) -> None:
        weather_service = WeatherService("https://meteofrance.com/previsions-meteo-france/")

        assert isinstance(weather_service, WeatherService)
        assert weather_service.url == "https://meteofrance.com/previsions-meteo-france/"
