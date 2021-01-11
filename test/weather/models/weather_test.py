from weather.models.weather import Weather

class TestClass(object):

    def test_weather(self) -> None:

        new_weather: Weather = Weather(30)

        assert isinstance(new_weather, Weather)
        assert new_weather.temperature == 30
