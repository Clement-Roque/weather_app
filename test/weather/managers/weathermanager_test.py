from weather.managers.weathermanager import WeatherManager

class TestWeatherManager(object):

    def test_weather_manager(self) -> None:

        weather_manager = WeatherManager()

        assert isinstance(weather_manager, WeatherManager)
