from temperatureEndpoint import MockedDataService, APICallingService, AbstractDataService

def test_mocked_data_service():
    service = MockedDataService()
    forecast = service.get_weather_forecast()
    assert forecast == {"forecast": "sunny", "temp": 25}

