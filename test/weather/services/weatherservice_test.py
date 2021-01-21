from weather.services.weatherservice import WeatherService

class TestWeatherService(object):

    def test_weather_service(self) -> None:

        weather_service = WeatherService()  # type: ignore
        assert weather_service.get_temperature() is None
        assert weather_service.get_weather_data() is None
