import sys
import re
import hashlib
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel, QMessageBox
from PyQt5.QtGui import QIcon
import sqlitedict  # SQLiteDict for storing data

class RegistrationApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Account Registration")
        self.setGeometry(100, 100, 400, 300)
        self.setWindowIcon(QIcon('python.ico'))

        # Initialize the SQLiteDict database
        self.db = sqlitedict.SqliteDict('accounts.db', autocommit=True)

        # Initialize UI components
        self.initUI()

    def initUI(self):
        # Create widgets
        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit(self)

        self.email_label = QLabel("Email:")
        self.email_input = QLineEdit(self)

        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)

        self.submit_button = QPushButton("Register", self)
        self.submit_button.clicked.connect(self.register_account)

        # Set layout
        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def register_account(self):
        # Get the input values
        username = self.username_input.text().strip()
        email = self.email_input.text().strip()
        password = self.password_input.text().strip()

        # Validate the inputs
        if not username or not email or not password:
            self.show_message("Error", "All fields must be filled in.", QMessageBox.Warning)
            return

        # Validate email format
        if not self.is_valid_email(email):
            self.show_message("Error", "Please enter a valid email address.", QMessageBox.Warning)
            return

        # Validate password strength (at least 8 characters, and should include numbers and letters)
        if len(password) < 8 or not re.search(r"[a-zA-Z]", password) or not re.search(r"[0-9]", password):
            self.show_message("Error", "Password must be at least 8 characters long, including letters and numbers.", QMessageBox.Warning)
            return

        # Check if the username already exists
        if username in self.db:
            self.show_message("Error", "Username already exists. Please choose another.", QMessageBox.Warning)
            return

        # Hash the password for storage (use hashlib)
        hashed_password = self.hash_password(password)

        # Save the account to the database
        self.db[username] = {"email": email, "password": hashed_password}

        # Show success message box
        self.show_message("Success", "Registration Successful!", QMessageBox.Information)

        # Clear input fields after successful registration
        self.username_input.clear()
        self.email_input.clear()
        self.password_input.clear()

    def hash_password(self, password):
        """ Hash the password using SHA-256 for secure storage """
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def is_valid_email(self, email):
        """ Validate the email format using regular expressions """
        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        return re.match(email_regex, email) is not None

    def show_message(self, title, message, icon_type):
        """ Show a message box with the given title, message, and icon type """
        msg = QMessageBox()
        msg.setIcon(icon_type)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RegistrationApp()
    window.show()
    sys.exit(app.exec_())
