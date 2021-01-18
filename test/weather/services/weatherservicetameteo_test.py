from weather.services.weatherservice import WeatherService
from weather.services.weatherservicetameteo import WeatherServiceTaMeteo

tameteo_ulr = "https://www.tameteo.com/meteo_Montpellier-Europe-France-Herault-LFMT-1-26126.html"

class TestWeatherServiceTaMeteo(object):

    def test_weather_service_weather_service_ta_meteo(self) -> None:
        weather_service_ta_meteo = WeatherServiceTaMeteo()

        assert isinstance(weather_service_ta_meteo, WeatherService)
        assert isinstance(weather_service_ta_meteo, WeatherServiceTaMeteo)
        assert weather_service_ta_meteo.url == tameteo_ulr

    def test_weather_service_weather_service_ta_meteo_get_temperature(self) -> None:
        weather_service_ta_meteo = WeatherServiceTaMeteo()

        ta_meteo_temperature = weather_service_ta_meteo.get_temperature()

        assert ta_meteo_temperature
        assert isinstance(ta_meteo_temperature, int)
