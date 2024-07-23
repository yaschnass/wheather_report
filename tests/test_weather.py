import pytest
import requests
from unittest.mock import patch
from weather_report import get_city, fetch_location, print_weather

# Mocking the fetch_location function
@pytest.fixture
def mock_weather_data():
    return {
        "name": "Test City",
        "weather": [{"description": "clear sky"}],
        "main": {
            "temp": 25,
            "feels_like": 27,
            "temp_min": 20,
            "temp_max": 30,
            "humidity": 60
        },
        "wind": {
            "speed": 15
        }
    } 

# Test for get_city
def test_get_city():
    assert get_city("New York") == "New York"
    assert get_city("") is None

# Test for fetch_location using requests-mock
@patch('requests.get')
def test_fetch_location(mock_get, mock_weather_data):
    mock_get.return_value.json.return_value = mock_weather_data
    city_name = "Test City"
    weather_data = fetch_location(city_name)
    
    assert weather_data["name"] == "Test City"
    assert weather_data["weather"][0]["description"] == "clear sky"
    assert weather_data["main"]["temp"] == 25

# Test for print_weather
def test_print_weather(mock_weather_data):
    with patch('builtins.print') as mock_print:
        print_weather(mock_weather_data)
    
        # Check if print was called with expected strings
        mock_print.assert_any_call("Today in Test City we have clear sky with the median temperature of 25°C.\n"
                                   "The minimum Temperature is 20°C and the maximum 30°C.\n")
        mock_print.assert_any_call("It feels like 27°C and the humidity is 60%")
        mock_print.assert_any_call('Windspeed: 29.16 knots, time to go KITING!')
    
        # Ensure that the snow-related print statement was not called
        assert not any("Snowfall: " in call[0] for call in mock_print.call_args_list)
