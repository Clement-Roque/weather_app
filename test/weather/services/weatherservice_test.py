from weather.services.weatherservice import WeatherService

class TestWeatherService(object):

    def test_weather_service(self) -> None:
        weather_service = WeatherService()

        assert isinstance(weather_service, WeatherService)
        assert "get_temperature" in weather_service.__dir__()

        assert weather_service.get_temperature() is False
