import sys
import io
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QMessageBox, QTextEdit
)
from PyQt5.QtGui import QFont
from hex_converter.converter import get_conversions
from hex_converter.utils import pretty_print_conversions

def capture_pretty_print(conv):
    buf = io.StringIO()
    sys_stdout = sys.stdout
    sys.stdout = buf
    try:
        pretty_print_conversions(conv)
    finally:
        sys.stdout = sys_stdout
    return buf.getvalue()

class HexConverterGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hex Converter")
        self.setFixedSize(600, 420)
        self.setStyleSheet("background: #191d21; color: #f5f6fa;")
        layout = QVBoxLayout()

        hlayout = QHBoxLayout()
        label = QLabel("Hex string:")
        label.setFont(QFont("Arial", 12))
        hlayout.addWidget(label)
        self.hex_input = QLineEdit()
        self.hex_input.setFont(QFont("Consolas", 13))
        self.hex_input.setStyleSheet("background: #23272f; color: #f5f6fa; border-radius: 8px; padding: 4px 8px;")
        hlayout.addWidget(self.hex_input)
        layout.addLayout(hlayout)

        self.convert_btn = QPushButton("Convert")
        self.convert_btn.setFont(QFont("Arial", 11))
        self.convert_btn.setStyleSheet("background: #00adb5; color: #fff; border-radius: 10px; padding: 6px 20px;")
        self.convert_btn.clicked.connect(self.convert_hex)
        layout.addWidget(self.convert_btn)

        self.result_box = QTextEdit()
        self.result_box.setFont(QFont("Consolas", 12))
        self.result_box.setStyleSheet("background: #23272f; color: #ffd369; border-radius: 10px;")
        self.result_box.setReadOnly(True)
        layout.addWidget(self.result_box)

        self.setLayout(layout)

    def convert_hex(self):
        hexstr = self.hex_input.text().strip()
        if not hexstr:
            return
        try:
            conv = get_conversions(hexstr)
            full_output = capture_pretty_print(conv)
            # Opțional, adaugi și endianness separat dacă nu e inclus
            full_output += (
                "\nHex representations:\n"
                f"Big endian:        {conv['Hex'][0]}\n"
                f"Mid-little endian: {conv['Hex'][1]}\n"
                f"Little endian:     {conv['Hex'][2]}\n"
            )
            self.result_box.setPlainText(full_output)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Invalid input:\n{e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = HexConverterGUI()
    win.show()
    sys.exit(app.exec_())
