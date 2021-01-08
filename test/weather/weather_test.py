from weather.weather import Weather


def test_weather():

    new_weather = Weather(30)

    assert isinstance(new_weather, Weather)
    assert new_weather.temperature == 30
