import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QFontDatabase
from PyQt6.QtCore import Qt, QTimer
import datetime as d

app = QApplication(sys.argv)

font_id = QFontDatabase.addApplicationFont("ProjectsResources/ds_digital/DS-DIGIB.TTF")

#Variable set for it

if font_id != -1:
    font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
else:
    font_family = "Arial"  # Fallback font if loading fails
    
window = QWidget()
window.setWindowTitle("Digital Clock")
window.setStyleSheet("background-color: black;")
window.showNormal()


timee = QLabel(d.datetime.now().strftime("%I:%M:%S %p"))
timee.setStyleSheet(f"""
                   font-family: '{font_family}';
                   font-size: 100px;
                   color: #249c0c;
                   """)
timee.setAlignment(Qt.AlignmentFlag.AlignCenter)

def update_timer():
    global timee
    
    now = d.datetime.now().strftime("%I:%M:%S %p")
 
    timee.setText(now)

layout = QVBoxLayout()


timer = QTimer()
timer.timeout.connect(update_timer)
timer.start(1000)

layout.addWidget(timee)

# Just Add it plj
window.setLayout(layout)

sys.exit(app.exec())

