import pytest
from typing import Any

from weather.models.weather import Weather
from weather.schemas.weatherschema import WeatherSchema

from .data.weather_schemas import basic_weather_data_json, basic_weather_data


@pytest.fixture
def basic_weather() -> Weather:
    return Weather(24)

class TestWheaterSchema(object):

    def test_weather_schema_weather_to_json(self, basic_weather: Weather) -> None:

        weather_schema: WeatherSchema = WeatherSchema()
        weather_json: Any = weather_schema.weather_to_json(basic_weather)

        assert isinstance(weather_json, str)

        assert weather_json == basic_weather_data_json

    def test_weather_schema_weather_from_json(self, basic_weather: Weather) -> None:
        weather_schema: WeatherSchema = WeatherSchema()
        weather_from_json: Weather = weather_schema.weather_from_json(basic_weather_data_json)

        assert isinstance(weather_from_json, Weather)
        assert weather_from_json.temperature == basic_weather.temperature

    def test_weather_schema_weather_from_data(self, basic_weather: Weather) -> None:

        weather_schema: WeatherSchema = WeatherSchema()
        weather_from_data: Weather = weather_schema.weather_from_data(basic_weather_data)

        assert isinstance(weather_from_data, Weather)
        assert weather_from_data.temperature == basic_weather.temperature
