from typing import Dict

from weather.services.weatherservice import WeatherService
from selenium import webdriver  # type: ignore

class WeatherServiceTaMeteo(WeatherService):

    def __init__(self) -> None:
        self.url = "https://www.tameteo.com/meteo_Montpellier-Europe-France-Herault-LFMT-1-26126.html"

    def get_temperature(self) -> int:

        browser: webdriver.WebDriver = webdriver.Firefox()
        browser.get(self.url)

        weather_temperature_from_browser: webdriver.WebElement = browser.find_element_by_class_name(
            "dato-temperatura").text

        browser.quit()

        ta_meteo_temperature = int(weather_temperature_from_browser.replace('°', '', 1))

        return ta_meteo_temperature

    def get_weather_data(self) -> Dict[str, int]:

        weather_data = {}

        weather_data["temperature"] = self.get_temperature()

        return weather_data
