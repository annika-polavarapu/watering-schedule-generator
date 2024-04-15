from urllib.request import urlopen
from urllib.error import URLError, HTTPError
import json
import abc

class AbstractDataService(metaclass=abc.ABCMeta):
    def get_weather_forecast(self):
        pass

# Data for testing
class MockedDataService(AbstractDataService):
    def get_weather_forecast(self):
        return {"forecast": "sunny", "temp": 25}
    
# API Calling Service
class APICallingService(AbstractDataService):
    def __init__(self, api_url):
        self.api_url = api_url

    def get_weather_forecast(self):
        try:
            with urlopen(self.api_url) as response:
                source = response.read()
                data = json.loads(source)
                return data
        except HTTPError as e:
            raise Exception(f"HTTP error: {e.code} {e.reason}")
        except URLError as e:
            raise Exception(f"URL error: {e.reason}")
        except json.JSONDecodeError:
            raise Exception("Error decoding JSON")
        
# Data Source Handler
class DataSourceHandler:
    def __init__(self, service: AbstractDataService):
        self.service = service

    def get_forecast(self):
        return self.service.get_weather_forecast()

# Builder function
def service_builder(config):
    if config["type"] == "mock":
        return MockedDataService()
    elif config["type"] == "api":
        return APICallingService(config["api_url"])

config = {
    "type": "mock",  # Change to api
    "api_url": "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m"
}

# Creating a service based on the config
service = service_builder(config)

# Create the handler
handler = DataSourceHandler(service)

# Get the forecast
forecast = handler.get_forecast()
print(f"The forecast data is: {forecast}")

