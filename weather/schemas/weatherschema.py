from marshmallow import Schema, fields, post_load
from typing import Dict, Union

from weather.models.weather import Weather


class WeatherSchema(Schema):
    temperature = fields.Int()

    @post_load  # type: ignore
    def make_weather(self: Schema, data: Dict[str, int], **kwargs: Union[str]) -> Weather:

        return Weather(**data)
