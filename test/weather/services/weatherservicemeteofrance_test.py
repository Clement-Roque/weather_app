from weather.services.weatherservice import WeatherService
from weather.services.weatherservicemeteofrance import WeatherServiceMeteoFrance

class TestWeatherServiceMeteoFrance(object):

    def test_weather_service_weather_service_meteo_france(self) -> None:
        weather_service_meteo_france = WeatherServiceMeteoFrance()

        assert isinstance(weather_service_meteo_france, WeatherService)
        assert isinstance(weather_service_meteo_france, WeatherServiceMeteoFrance)
        assert weather_service_meteo_france.url == "https://meteofrance.com/previsions-meteo-france/montpellier/34000"
