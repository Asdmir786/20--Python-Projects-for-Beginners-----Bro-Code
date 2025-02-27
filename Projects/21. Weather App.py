import sys
import requests
import datetime
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QPushButton
from PyQt6.QtCore import Qt 
from PyQt6.QtGui import QPixmap

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.showNormal()
        self.setWindowTitle("Weather App")
        
        self.city_input = QLineEdit()
        self.city_input.setPlaceholderText("Enter City")
        self.city_input.setFixedWidth(200)
        self.city_input.setStyleSheet(
            "QLineEdit { padding: 10px; font-size: 15px; font-family: Arial; }"
        )
        # self.city_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.temp = QPushButton("") # e.g 72°F
        self.temp.setStyleSheet("border: None; ")
        self.feel_temp = QPushButton("")  # e.g. Feels like 72°F
        self.feel_temp.setStyleSheet("border: None; ")
        self.description = QLabel("")     # e.g. Rainy
        self.time = QPushButton("")       # e.g. 27/02/2025 01:48:44 PM
        self.time.setStyleSheet("border: None; ")
        self.day_parts = QLabel("")       # e.g. afternoon
        self.day_parts.setStyleSheet("border: None; ")
        self.label_weather_icon = QLabel()
        self.weather_icon = QPixmap()
        self.label_weather_icon.setPixmap(self.weather_icon)
        self.status_code = QLabel()
        
        hbox = QHBoxLayout()
        hbox.addWidget(self.temp)
        hbox.addWidget(self.feel_temp)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.city_input, alignment=Qt.AlignmentFlag.AlignCenter)
        vbox.addLayout(hbox)
        vbox.addWidget(self.description)
        vbox.addWidget(self.time)
        vbox.addWidget(self.day_parts)
        vbox.addWidget(self.label_weather_icon)
        vbox.addWidget(self.status_code)
        self.setLayout(vbox)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

# Replace with your actual API key
api_key = "384a7841f7fdedeb6bbff308c6d50713"
city = "Lahore"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# Send the request
response = requests.get(url)
data = response.json()

# Extract relevant details
temperature = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
description = data["weather"][0]["description"]
weather_code = data["weather"][0]["id"]

# Instead of mapping weather code to an emoji, use the provided icon code
icon_code = data["weather"][0]["icon"]  # e.g., "10d" or "01n"
icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"

# Create a timezone object using the API's timezone offset (in seconds)
timezone_offset = data["timezone"]
tz_local = datetime.timezone(datetime.timedelta(seconds=timezone_offset))

# Convert Unix timestamps to local time using datetime.fromtimestamp() with tz parameter
current_time_local = datetime.datetime.fromtimestamp(data["dt"], tz=tz_local)
# The sunrise and sunset values are used to help determine if it's day or night
sunrise = data["sys"]["sunrise"]
sunset = data["sys"]["sunset"]

# Determine the time of day
if data["dt"] < sunrise or data["dt"] > sunset:
    time_of_day = "night"
else:
    hour = current_time_local.hour
    if 6 <= hour < 12:
        time_of_day = "morning"
    elif 12 <= hour < 18:
        time_of_day = "afternoon"
    elif 18 <= hour < 21:
        time_of_day = "evening"
    else:
        time_of_day = "daytime"

# Print the collected information
print(f"Temperature: {temperature} °C")
print(f"Feels like: {feels_like} °C")
print(f"Description: {description}")
print(f"Weather code: {weather_code}")
print(f"Current local time: {current_time_local.strftime('%d/%m/%Y %I:%M:%S %p')}")
print(f"It's currently: {time_of_day}")
print(f"Weather icon URL: {icon_url}")
print(f"Status Code: {data["cod"]}")
