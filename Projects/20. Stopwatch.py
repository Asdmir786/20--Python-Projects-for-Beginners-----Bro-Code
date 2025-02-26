import sys
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QWidget
from PyQt6.QtCore import QTime, QTimer, Qt

# Create the application
app = QApplication(sys.argv)

# Initialize main window
main_window = QWidget()
main_window.setWindowTitle("Digital Stopwatch.")
main_window.showNormal()

# Set up layouts: vbox for overall layout and hbox for button grouping
vbox = QVBoxLayout()  
hbox = QHBoxLayout()  

# Create widgets
stopwatch_timer = QLabel("00:00:00.00")
start_button = QPushButton("Start")
stop_button = QPushButton("Stop")
reset_button = QPushButton("Reset")

# Customize the timer appearance and center the text
stopwatch_timer.setStyleSheet('''
                              background-color: #00ccff;
                              border-radius: 20px;
                              font-size: 100px;
                              font-family: Calibri;
                              font-weight: bold;
                              color: #1b1e1f;
                              ''')
stopwatch_timer.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center timer text

# Customize button appearances
start_button.setStyleSheet('''
                           padding-top: 30px;
                           padding-bottom: 30px;
                           padding-left: 30px;
                           padding-right: 30px;
                           font-size: 40px;
                           font-family: Calibri;
                           font-weight: bold;
                           ''')
stop_button.setStyleSheet('''
                           padding-top: 30px;
                           padding-bottom: 30px;
                           padding-left: 30px;
                           padding-right: 30px;
                           font-size: 40px;
                           font-family: Calibri;
                           font-weight: bold;
                           ''')
reset_button.setStyleSheet('''
                           padding-top: 30px;
                           padding-bottom: 30px;
                           padding-left: 30px;
                           padding-right: 30px;
                           font-size: 40px;
                           font-family: Calibri;
                           font-weight: bold;
                           ''')

timer = QTimer()
elapsed_time = QTime(0, 0, 0, 0)

def update_timer():
    global elapsed_time
    elapsed_time = elapsed_time.addMSecs(10)
    formatted_time = elapsed_time.toString("hh:mm:ss.zzz")
    stopwatch_timer.setText(formatted_time)

def start_timer():
    timer.start(10)

def stop_timer():
    timer.stop()

def reset_timer():
    timer.stop()
    global elapsed_time
    elapsed_time = QTime(0, 0, 0, 0)
    stopwatch_timer.setText("00:00:00.00")

timer.timeout.connect(update_timer)
start_button.clicked.connect(start_timer)
stop_button.clicked.connect(stop_timer)
reset_button.clicked.connect(reset_timer)

# Add the timer widget and buttons to the layouts
vbox.addWidget(stopwatch_timer)
hbox.addWidget(start_button)
hbox.addWidget(stop_button)
hbox.addWidget(reset_button)

# Combine the horizontal layout into the vertical layout and set it for the window
vbox.addLayout(hbox)
main_window.setLayout(vbox)


# Start the event loop
sys.exit(app.exec())