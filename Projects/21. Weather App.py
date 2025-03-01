import sys
import time
import requests
import datetime
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QPushButton
from PyQt6.QtCore import Qt, QTimer
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
            "QLineEdit { margin: 0; padding: 10px; font-size: 15px; font-family: Arial; }"
        )
        self.city_input.returnPressed.connect(self.get_info_and_set)
        
        self.submit_button = QPushButton("Submit")
        self.submit_button.setFixedWidth(100)
        self.submit_button.setStyleSheet("padding: 10px;")
        self.submit_button.clicked.connect(self.check_for_input_text)
        
        self.city_country = QLabel("") # e.g. Lahore, PK
        self.city_country.setStyleSheet("font-size: 40px; margin: 0;")
        
        self.temp = QPushButton("")  # e.g 72°F
        self.temp.setStyleSheet("border: none; font-size: 40px; margin-top: 40px;")
        self.temp.setFixedWidth(200)
        self.temp.clicked.connect(self.change_temp_on_click)
        
        self.feel_temp = QPushButton("")  # e.g. Feels like 72°F
        self.feel_temp.setStyleSheet("border: none; margin: 0; ")
        self.feel_temp.setFixedWidth(100)
        
        self.description = QLabel("")      # e.g. Rainy
        self.description.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.description.setStyleSheet("font-size: 40px;")
        
        self.time = QPushButton("")  # e.g. 27/02/2025 01:48:44 PM
        self.time.setStyleSheet("border: None; ")
        self.time.clicked.connect(self.change_date_on_click)
        
        self.day_parts = QLabel("")       # e.g. afternoon
        self.day_parts.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.day_parts.setStyleSheet("border: None; ")
        
        self.label_weather_icon = QLabel()
        self.weather_icon = QPixmap()
        
        self.label_weather_icon.setPixmap(self.weather_icon)
        self.status_code = QLabel()
        
        hbox = QHBoxLayout()
        hbox.setSpacing(15)  # No extra spacing between widgets
        hbox.setContentsMargins(0, 0, 0, 0)  # No layout margins
        hbox.addWidget(self.city_input)
        hbox.addWidget(self.submit_button)
        hbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(self.city_country, alignment=Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(self.temp, alignment=Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(self.feel_temp, alignment=Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(self.description, alignment=Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(self.time, alignment=Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(self.day_parts, alignment=Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(self.label_weather_icon, alignment=Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(self.status_code, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(vbox)
    
    def change_temp_on_click(self):
        feel_temp = self.feel_temp.text()
        feel_temp = feel_temp.split(" ")
        del feel_temp[0:2]

        temp = self.temp.text()
        temp = temp.split()

        if temp[1] == "°C":
            feel_temp = float(feel_temp[0])
            Ffeel_temp = (feel_temp * (9/5)) + 32
            
            temp = float(temp[0])
            Ftemp = (temp * (9/5)) + 32
            self.temp.setText(f"{Ftemp:.2f} °F")
            self.feel_temp.setText(f"Feels like {Ffeel_temp:.2f} °F")
        elif temp[1] == "°F":
            feel_temp = float(feel_temp[0])
            Ffeel_temp = (feel_temp - 32) * (5/9)
                        
            temp = float(temp[0])
            Ftemp = (temp - 32) * (5/9)
            self.temp.setText(f"{Ftemp:.2f} °C")
            self.feel_temp.setText(f"Feels like {Ffeel_temp:.2f} °C")
        else:
            print("Cheen Tapak Dam Dam.")
           
    def change_date_on_click(self):
        Dtime = self.time.text()
        Dtime = datetime.datetime.strptime(Dtime, "%d/%m/%Y %I:%M:%S %p")
        Dtime = datetime.datetime.strftime(Dtime, "%d/%m/%Y %H:%M:%S")
        print(f"{Dtime}, {type(Dtime)}\n{self.data}")
            
    def get_info_and_set(self):
        if not(self.city_input.text().capitalize().strip()):
            self.submit_button.setText("Enter a city ching bong.")
            time.sleep(2)
            self.submit_button.setText("Submit")

        city = self.city_input.text().capitalize().strip()

        api_key = "384a7841f7fdedeb6bbff308c6d50713"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        self.data = response.json()
        
        if self.data["cod"] == 200:
            # Extract relevant details
            temperature = self.data["main"]["temp"]
            feels_like = self.data["main"]["feels_like"]
            description = self.data["weather"][0]["description"]
            weather_code = self.data["weather"][0]["id"]
            data_city = self.data["name"]
            data_country = self.data["sys"]["country"]
            
            # Instead of mapping weather code to an emoji, use the provided icon code
            icon_code = self.data["weather"][0]["icon"]  # e.g., "10d" or "01n"
            icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"

            # Create a timezone object using the API's timezone offset (in seconds)
            timezone_offset = self.data["timezone"]
            tz_local = datetime.timezone(datetime.timedelta(seconds=timezone_offset))

            # Convert Unix timestamps to local time using datetime.fromtimestamp() with tz parameter
            current_time_local = datetime.datetime.fromtimestamp(self.data["dt"], tz=tz_local)
            # The sunrise and sunset values are used to help determine if it's day or night
            sunrise = self.data["sys"]["sunrise"]
            sunset = self.data["sys"]["sunset"]

            # Determine the time of day
            if self.data["dt"] < sunrise or self.data["dt"] > sunset:
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

            self.city_country.setText(f"{data_city}, {data_country}")
            self.temp.setText(f"{temperature} °C")
            self.feel_temp.setText(f"Feels like: {feels_like} °C")
            self.description.setText(description)
            self.time.setText(current_time_local.strftime('%d/%m/%Y %I:%M:%S %p'))
            self.day_parts.setText(time_of_day)
            
            icon_response = requests.get(icon_url)
            if icon_response.status_code == 200:
                self.weather_icon.loadFromData(icon_response.content)
                self.label_weather_icon.setPixmap(self.weather_icon)
            else:
                print("Failed to download the icon image")
            
            # Print the collected information
            # print(f"Temperature: {temperature} °C")
            # print(f"Feels like: {feels_like} °C")
            # print(f"Description: {description}")
            # print(f"Weather code: {weather_code}")
            # print(f"Current local time: {current_time_local.strftime('%d/%m/%Y %I:%M:%S %p')}")
            # print(f"It's currently: {time_of_day}")
            # print(f"Weather icon URL: {icon_url}")
            # print(f"Status Code: {self.data["cod"]}")
        else:
            self.status_code_display(self.data["cod"])

    def check_for_input_text(self):
        if len(self.city_input.text().strip()) != 0:
            self.get_info_and_set()
        else:
            self.submit_button.setText("Enter a city.")
            QTimer.singleShot(2000, lambda: self.submit_button.setText("Submit"))
    
    def do_nothing(self):
        pass
    
    def status_code_display(self, code):
        try:
            code_int = int(code)
        except ValueError:
            self.status_code.setText(f"Invalid status code: {code}")
            return
        error_messages = {
            200: "Success: Weather data retrieved.",
            401: "Error 401: Unauthorized – Invalid API key.",
            404: "Error 404: City not found.",
            429: "Error 429: Too many requests – Please slow down.",
            500: "Error 500: Internal server error.",
            502: "Error 502: Bad Gateway.",
            503: "Error 503: Service Unavailable.",
            504: "Error 504: Gateway Timeout."
        }
        message = error_messages.get(code_int, f"Unexpected status code: {code}")
        self.status_code.setText(message)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())


