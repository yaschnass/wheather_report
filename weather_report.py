import requests

API_ROOT="https://api.openweathermap.org/data/2.5/weather?q="
API_USER="&appid=YOUROPENWHEATERMAPAPI&units=metric"

API_CITY=input("Where in the world are you?:\n")
def get_city():
    while True:
        if len(API_CITY)==len(API_CITY)>0:
            print_weather()
            break
        
        else:
            print("I don't know this city, try again")

def fetch_location():
    full_api=API_ROOT+API_CITY+API_USER

    return requests.get(full_api).json()



weather_data = fetch_location()
city=weather_data["name"]
main_weather=weather_data["weather"][0]["description"]
temp=weather_data["main"]["temp"]
feels_like=weather_data["main"]["feels_like"]
temp_min=weather_data["main"]["temp_min"] 
temp_max=weather_data["main"]["temp_max"] 
humidity=weather_data["main"]["humidity"] 
wind_speed=(weather_data["wind"]["speed"]*1.943844)

def print_weather():
    print(f"Today in {city} we have {main_weather} with the median temperature of {temp}°C.\n"
        f"The minimum Temperature is {temp_min}°C and the maximum {temp_max}°C.\n")
    print(f"It feels like {feels_like}°C and the humidity is {humidity}%")
    if wind_speed>=15:
        
        print(f"Windspeed: {wind_speed:.2f}knots, time to go KITING !")
    else:
        print(f"Windspeed: {wind_speed:.2f}knots, no kiting today :(")

    if "snow" in weather_data:
        snow=weather_data["snow"]["1h"]
        print(f"Snowfall: {snow}mm/h")
get_city()
