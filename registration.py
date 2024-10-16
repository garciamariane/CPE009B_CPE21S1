# registration.py
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFormLayout, QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Account Registration System")
        self.setGeometry(100, 100, 400, 400)
        self.setWindowIcon(QIcon('pythonico.ico'))

        # Create the title label
        title = QLabel("Account Registration", self)
        title.setAlignment(Qt.AlignCenter)

        # Create input fields and labels
        self.first_name = QLineEdit(self)
        self.last_name = QLineEdit(self)
        self.username = QLineEdit(self)
        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.Password)
        self.email = QLineEdit(self)
        self.contact_number = QLineEdit(self)

        # Layouts
        form_layout = QFormLayout()
        form_layout.addRow(QLabel("First Name:"), self.first_name)
        form_layout.addRow(QLabel("Last Name:"), self.last_name)
        form_layout.addRow(QLabel("Username:"), self.username)
        form_layout.addRow(QLabel("Password:"), self.password)
        form_layout.addRow(QLabel("Email Address:"), self.email)
        form_layout.addRow(QLabel("Contact Number:"), self.contact_number)

        # Buttons
        self.submit_button = QPushButton("Submit", self)
        self.clear_button = QPushButton("Clear", self)

        # Connect buttons
        self.submit_button.clicked.connect(self.submit)
        self.clear_button.clicked.connect(self.clear)

        # Bottom layout
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.submit_button)
        button_layout.addWidget(self.clear_button)

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(title)
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def submit(self):
        # Here you can add logic to handle form submission
        print("Form submitted.")
        # Example: print the entered data
        print("First Name:", self.first_name.text())
        print("Last Name:", self.last_name.text())
        print("Username:", self.username.text())
        print("Password:", self.password.text())
        print("Email:", self.email.text())
        print("Contact Number:", self.contact_number.text())

    def clear(self):
        # Clear all fields
        self.first_name.clear()
        self.last_name.clear()
        self.username.clear()
        self.password.clear()
        self.email.clear()
        self.contact_number.clear()

