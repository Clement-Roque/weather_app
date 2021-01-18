from weather.services.weatherservice import WeatherService
from selenium import webdriver  # type: ignore


class WeatherServiceMeteoFrance(WeatherService):

    def __init__(self):
        super(WeatherService, self).__init__()
        self.url = "https://meteofrance.com/previsions-meteo-france/montpellier/34000"

    def get_temperature(self) -> int:

        browser: webdriver.WebDriver = webdriver.Firefox()
        browser.get(self.url)

        weather_temperature_from_browser: webdriver.WebElement = browser.find_element_by_class_name("temp").text

        browser.quit()

        weather_temperature = int(weather_temperature_from_browser.replace('°', '', 1))

        return weather_temperature
