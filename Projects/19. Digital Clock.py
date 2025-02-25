import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QFontDatabase
from PyQt6.QtCore import Qt

app = QApplication(sys.argv)

font_id = QFontDatabase.addApplicationFont("ProjectsResources/ds_digital/DS-DIGIT.TTF")
if font_id != -1:
    font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
else:
    font_family = "Arial"  # Fallback font if loading fails
    
window = QWidget()
window.setWindowTitle("Digital Clock")
window.showNormal()

time = QLabel("00:00:00")
time.setStyleSheet(f"""
                   font-family: '{font_family}';
                   font-size: 100px;
                   """)
time.setAlignment(Qt.AlignmentFlag.AlignCenter)

layout = QVBoxLayout()

layout.addWidget(time)

# Just Add it plj
window.setLayout(layout)

sys.exit(app.exec())

