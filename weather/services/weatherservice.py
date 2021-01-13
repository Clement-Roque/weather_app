from selenium import webdriver  # type: ignore


class WeatherService(object):

    def __init__(self, url: str):
        super(WeatherService, self).__init__()
        self.url = url

    def get_temperature(self) -> int:

        browser: webdriver.WebDriver = webdriver.Firefox()
        browser.get(self.url)

        weather_temperature_from_browser: webdriver.WebElement = browser.find_element_by_class_name("temp").text

        browser.quit()

        weather_temperature = int(weather_temperature_from_browser.replace('°', '', 1))

        return weather_temperature
