from pytest_socket import disable_socket, enable_socket  # type: ignore

from weather.services.weatherservicefacade import WeatherServiceFacade
from weather.services.weatherservice import WeatherService
from test.weather.schemas.data.weather_schemas import weather_schema_fields


class TestWeatherServiceFacade(object):

    def test_weather_service_facade(sefl) -> None:

        weather_service_facade: WeatherServiceFacade = WeatherServiceFacade()

        assert len(weather_service_facade.weather_services) > 0

        for weather_service in weather_service_facade.weather_services:

            assert isinstance(weather_service(), WeatherService)  # type: ignore

    def test_weather_service_facade_get_weather_data(self) -> None:

        weather_service_facade: WeatherServiceFacade = WeatherServiceFacade()

        facade_weather_data = weather_service_facade.get_weather_data()

        assert isinstance(facade_weather_data, dict)

        assert weather_schema_fields == list(facade_weather_data.keys())

    def test_weather_service_facade_dont_get_weather_data(self) -> None:

        disable_socket()

        weather_service_facade: WeatherServiceFacade = WeatherServiceFacade()

        facade_weather_data = weather_service_facade.get_weather_data()

        assert isinstance(facade_weather_data, dict)

        assert facade_weather_data == {}

        enable_socket()
