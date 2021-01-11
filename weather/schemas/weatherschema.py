from marshmallow import Schema, fields, post_load

from weather.models.weather import Weather


class WeatherSchema(Schema):
    temperature = fields.Int()

    @post_load  # type: ignore
    def make_weather(self: Schema, data: dict, **kwargs) -> Weather:

        return Weather(**data)
