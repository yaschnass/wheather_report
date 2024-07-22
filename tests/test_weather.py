import pytest
from unittest.mock import patch, MagicMock
import io
import sys
from weather import get_city, fetch_location, print_weather, main

# Test for get_city function
def test_get_city():
    assert get_city("New York") == "New York"
    assert get_city("") is None

# Test for fetch_location function
@patch('requests.get')
def test_fetch_location(mock_get):
    # Mock the JSON response
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "name": "New York",
        "weather": [{"description": "clear sky"}],
        "main": {
            "temp": 25,
            "feels_like": 27,
            "temp_min": 20,
            "temp_max": 30,
            "humidity": 60
        },
        "wind": {"speed": 10}
    }
    mock_get.return_value = mock_response
    
    result = fetch_location("New York")
    assert result["name"] == "New York"
    assert result["weather"][0]["description"] == "clear sky"

# Test for print_weather function
@patch('sys.stdout', new_callable=io.StringIO)
def test_print_weather(mock_stdout):
    weather_data = {
        "name": "New York",
        "weather": [{"description": "clear sky"}],
        "main": {
            "temp": 25,
            "feels_like": 27,
            "temp_min": 20,
            "temp_max": 30,
            "humidity": 60
        },
        "wind": {"speed": 10}
    }
    print_weather(weather_data)
    
    output = mock_stdout.getvalue()
    print("output from print_weather:", output)
    assert "Today in New York we have clear sky with the median temperature of 25°C." in output
    assert "The minimum Temperature is 20°C and the maximum 30°C." in output
    assert "It feels like 27°C and the humidity is 60%" in output
    assert "Windspeed: 19.44 knots, no kiting today :(" in output

# Test for main function
@patch('builtins.input', return_value='New York')
@patch('your_module.fetch_location')
@patch('your_module.print_weather')
def test_main(mock_print_weather, mock_fetch_location, mock_input):
    # Mock the return value of fetch_location
    mock_fetch_location.return_value = {
        "name": "New York",
        "weather": [{"description": "clear sky"}],
        "main": {
            "temp": 25,
            "feels_like": 27,
            "temp_min": 20,
            "temp_max": 30,
            "humidity": 60
        },
        "wind": {"speed": 10}
    }
    
    with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
        main()
        output = mock_stdout.getvalue()
        assert "Today in New York we have clear sky with the median temperature of 25°C." in output

