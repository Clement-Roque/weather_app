from weather.managers.weathermanager import WeatherManager
from weather.models.weather import Weather

class TestWeatherManager(object):

    def test_weather_manager(self) -> None:

        weather_manager = WeatherManager()

        assert isinstance(weather_manager, WeatherManager)

    def tests_get_current_weather(self) -> None:

        weather_manager = WeatherManager()

        weather = weather_manager.get_current_weather()

        assert isinstance(weather, Weather)
        # assert isinstance(weather.)
