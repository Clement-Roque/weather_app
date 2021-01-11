from weather.models.weather import Weather


def test_weather() -> None:

    new_weather: Weather = Weather(30)

    assert isinstance(new_weather, Weather)
    assert new_weather.temperature == 30
