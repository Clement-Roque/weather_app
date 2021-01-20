import pytest
from typing import Any

from weather.models.weather import Weather
from weather.schemas.weatherschema import WeatherSchema

from .data.weather_schemas import basic_weather_schema


@pytest.fixture
def basic_weather() -> Weather:
    return Weather(24)

class TestWheaterSchema(object):

    def test_weather_schema_weather_to_json(self, basic_weather: Weather) -> None:

        weather_schema: WeatherSchema = WeatherSchema()
        weather_json: Any = weather_schema.weather_to_json(basic_weather)

        assert isinstance(weather_json, str)

        assert weather_json == basic_weather_schema

    def test_weather_schema_weather_from_json(self, basic_weather: Weather) -> None:
        weather_schema: WeatherSchema = WeatherSchema()
        weather_from_json: Weather = weather_schema.weather_from_json(basic_weather_schema)

        assert isinstance(weather_from_json, Weather)
        assert weather_from_json.__dict__ == basic_weather.__dict__
        assert weather_from_json.temperature == basic_weather.temperature
