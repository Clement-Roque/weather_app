from marshmallow import Schema, fields, post_load
from typing import Dict, Union, Any

from weather.models.weather import Weather


class WeatherSchema(Schema):
    temperature = fields.Int()

    @post_load  # type: ignore
    def make_weather(self: Schema, data: Dict[str, int], **kwargs: Union[str]) -> Weather:

        return Weather(**data)

    def weather_to_json(self: Schema, weather: Weather) -> Any:

        return self.dumps(weather)

    def weather_from_json(self: Schema, weather_json: Any) -> Weather:

        weather: Weather = self.loads(weather_json)

        return weather
