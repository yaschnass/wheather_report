# Weather Information Script

This Python script retrieves and displays weather information for a given city using the OpenWeatherMap API.

## Features

- Fetches current weather data for a specified city.
- Displays weather description, temperature, humidity, and wind speed.
- Provides a recommendation based on wind speed.
- Displays snowfall information if available.

## Requirements

- Python 3.x
- `requests` library

## Setup

1. **Install the `requests` library** if you haven't already:
    ```bash
    pip install requests
    ```

2. **Get an API Key** from [OpenWeatherMap](https://openweathermap.org/api) and replace the placeholder in the script with your API key.

## Usage

1. **Run the script**:
    ```bash
    python weather_script.py
    ```

2. **Input the city name** when prompted. The script will:
   - Fetch weather data for the specified city.
   - Display current weather conditions, including temperature, humidity, and wind speed.
   - Provide a message based on the wind speed.
   - Show snowfall information if present.

### Example

When prompted:

```plaintext
Where in the world are you?:
```

Enter the city name, e.g., `New York`, and the script will fetch and display the weather information.

## Functions

- **`fetch_location()`**: Retrieves weather data from the OpenWeatherMap API.
- **`print_weather()`**: Displays weather information including temperature, humidity, wind speed, and snowfall.
- **`get_city()`**: Prompts user for a city and initiates weather data retrieval.

## Notes

- Ensure that the API key is correctly replaced in the script.
- The script expects a valid city name and will prompt the user again if an invalid city is entered.

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Submit a pull request with a description of your changes.
