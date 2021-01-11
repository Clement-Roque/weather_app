import pytest

from weather.models.weather import Weather
from weather.schemas.weatherschema import WeatherSchema

from .data.weather_schemas import basic_weather_schema


@pytest.fixture
def basic_weather() -> Weather:
    return Weather(24)

class TestWheaterSchema(object):

    def test_weather_schema_weather_to_json(self, basic_weather) -> None:
        weather_schema: WeatherSchema = WeatherSchema()

        assert weather_schema.dumps(basic_weather) == basic_weather_schema

    def test_weather_schema_json_to_weather(self, basic_weather) -> None:
        weather_schema: WeatherSchema = WeatherSchema()
        weather_from_json: Weather = weather_schema.loads(basic_weather_schema)

        assert isinstance(weather_from_json, Weather)
        assert weather_from_json.temperature == basic_weather.temperature
