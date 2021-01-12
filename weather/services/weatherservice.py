class WeatherService(object):
    """docstring for WeatherService"""

    def __init__(self, url: str):
        super(WeatherService, self).__init__()
        self.url = url
