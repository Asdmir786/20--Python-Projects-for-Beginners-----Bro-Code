# import datetime as d 

# days = 1
# hours = 12
# minutes = 42
# seconds = 58

# current_time = d.datetime.now().strftime("%d %H:%M:%S")
# user_date = d.datetime.now().replace(day=days,hour=hours,minute=minutes,second=seconds,microsecond=0).strftime("%d %H:%M:%S")

# print(current_time)
# print("="*12)
# print(user_date)
import datetime as d
import time
# from keyboard import wait
# import pathlib

# path = pathlib.Path("ProjectsResources/Audios")
# audios = [audio for audio in path.iterdir()]

# def set_alarm(user_date="", audio_number = 0):
#     parts = user_date.split(":")
#     hourss,minutess,secondss = map(int,parts)
#     time_to_blyat = d.time(hourss,minutess,secondss)

#     while True:
#         current_time = d.datetime.now().strftime("%H:%M:%S")
#         if current_time == str(time_to_blyat):
#             print(f"{current_time} = {time_to_blyat}")
#             break
#         else:
#             print(current_time)
#             print(type(current_time))
#             time.sleep(1)

# set_alarm("23:11:00")

# now = d.datetime.now().strftime("%H:%M:%S")

# while True:
#     time.sleep(0.1)
#     new_now = d.datetime.now().strftime("%H:%M:%S")

#     if new_now == now:
#         print(f"{now} : {new_now} are Same.")   
#     else:
#         print(f"{now} : {new_now}")
#         now = d.datetime.now().strftime("%H:%M:%S")

# import sys
# from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
# from PyQt6.QtCore import QTimer, Qt

# app = QApplication(sys.argv)

# # Create a main window and a label to display the counter
# window = QMainWindow()
# window.setWindowTitle("Counter Timer")
# label = QLabel("0")
# label.setAlignment(Qt.AlignmentFlag.AlignCenter)
# window.setCentralWidget(label)
# window.resize(200, 100)
# window.show()

# counter = 0

# def update_counter():
#     global counter
#     counter += 1
#     label.setText(str(counter))

# # Set up a timer that calls update_counter every 1000ms (1 second)
# timer = QTimer()
# timer.timeout.connect(update_counter)
# timer.start(1000)

# sys.exit(app.exec())

import requests

def geocode_city(city_name):
    """
    Look up a city using the Open-Meteo Geocoding API.

    Args:
        city_name (str): The name of the city to look up.

    Returns:
        tuple: A tuple (latitude, longitude, resolved_city_name). 
               Returns (None, None, None) if the city is not found.
    """
    # API endpoint for city geocoding
    url = "https://geocoding-api.open-meteo.com/v1/search"
    # Parameters for the API call: the city name and count=1 to get the first match
    params = {"name": city_name, "count": 1}
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        results = data.get("results")
        if results:
            # Use the first result from the returned list
            result = results[0]
            return result["latitude"], result["longitude"], result["name"]
    # If the API call fails or no city is found, return None values
    return None, None, None

def map_weather_code(code):
    """
    Convert a numeric weather code into a text description and emoji.

    Args:
        code (int): The weather code from the API.

    Returns:
        tuple: (description, emoji) representing the weather condition.
    """
    if code == 0:
        return "Clear sky", "☀️"
    elif code in [1, 2, 3]:
        return "Partly cloudy", "⛅"
    elif code in [45, 48]:
        return "Foggy", "🌫️"
    elif code in [51, 53, 55]:
        return "Drizzle", "🌦️"
    elif code in [56, 57]:
        return "Freezing drizzle", "🌧️"
    elif code in [61, 63, 65]:
        return "Rain", "🌧️"
    elif code in [66, 67]:
        return "Freezing rain", "🥶"
    elif code in [71, 73, 75]:
        return "Snow", "❄️"
    elif code == 77:
        return "Snow grains", "❄️"
    elif code in [80, 81, 82]:
        return "Rain showers", "🌦️"
    elif code in [85, 86]:
        return "Snow showers", "🌨️"
    elif code in [95, 96, 99]:
        return "Thunderstorm", "⛈️"
    else:
        return "Unknown", "❓"

def get_weather(latitude, longitude):
    """
    Retrieve current weather and hourly apparent temperature data using the Open-Meteo API.

    Args:
        latitude (float): The latitude of the location.
        longitude (float): The longitude of the location.

    Returns:
        dict: A dictionary containing the weather data if successful; otherwise, None.
    """
    # API endpoint for weather forecast
    url = "https://api.open-meteo.com/v1/forecast"
    # Set up parameters for current weather and hourly apparent temperature data
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": "true",  # Request current weather info (temperature, wind speed, etc.)
        "hourly": "apparent_temperature",  # Request hourly "feels like" temperature
        "timezone": "auto"  # Automatically adjust to the local timezone
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching weather data:", response.status_code)
        return None

if __name__ == "__main__":
    # Ask the user to enter a city name
    city = input("Enter a city name: ")
    # Get the location details (latitude, longitude, and city name)
    lat, lon, resolved_name = geocode_city(city)
    
    if lat is None:
        print("City not found. Please try a different city name.")
    else:
        print(f"Location: {resolved_name} (lat: {lat}, lon: {lon})")
        # Fetch weather data for the specified location
        data = get_weather(lat, lon)
        if data:
            # Extract current weather information and hourly data from the API response
            current = data.get("current_weather", {})
            hourly = data.get("hourly", {})
            current_time = current.get("time")  # Current time in ISO 8601 format
            temperature = current.get("temperature")
            weather_code = current.get("weathercode")
            
            # Find the "apparent_temperature" for the current time
            apparent_temp = None
            times = hourly.get("time", [])
            apparent_values = hourly.get("apparent_temperature", [])
            if current_time and times and apparent_values:
                try:
                    # Look for the current time in the list of hourly times
                    idx = times.index(current_time)
                    apparent_temp = apparent_values[idx]
                except ValueError:
                    # If current time is not found, leave apparent_temp as None
                    pass

            # Convert the numeric weather code to a description and emoji
            description, emoji = map_weather_code(weather_code)
            
            # Display the weather information to the user
            print(f"Current Temperature: {temperature}°C")
            if apparent_temp is not None:
                print(f"Feels Like: {apparent_temp}°C")
            print(f"Condition: {description} (Code: {str(weather_code).zfill(3)}) {emoji}")
        else:
            print("Failed to retrieve weather data.")