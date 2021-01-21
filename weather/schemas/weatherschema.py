from marshmallow import Schema, fields, post_load
from typing import Dict, Union, Any

from weather.models.weather import Weather


class WeatherSchema(Schema):
    temperature = fields.Int()

    @post_load  # type: ignore
    def make_weather(self: Schema, data: Dict[str, int], **kwargs: Union[str]) -> Weather:

        return Weather(**data)

    def weather_to_json(self: Schema, weather: Weather) -> str:

        weather_json: str = self.dumps(weather)

        return weather_json

    def weather_from_json(self: Schema, weather_json: Any) -> Weather:

        weather: Weather = self.loads(weather_json)

        return weather

    def weather_from_data(self, weather_data: Dict[str, int]) -> Weather:

        weather: Weather = self.load(weather_data)

        return weather
