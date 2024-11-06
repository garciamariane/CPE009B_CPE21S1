import tkinter as tk
import math
from tkinter import messagebox
from tkinter import filedialog

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x600")
        
        self.expression = ""
        self.result = ""
        
        # Create the GUI layout
        self.create_widgets()
        self.create_menus()

    def create_widgets(self):
        # Entry to display the expression/result
        self.display = tk.Entry(self.root, font=("Arial", 24), borderwidth=2, relief="solid", justify="right", bd=10)
        self.display.grid(row=0, column=0, columnspan=4)
        
        # Buttons for numbers and operations
        button_texts = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+",
            "sin", "cos", "exp", "C"
        ]
        
        # Create buttons dynamically based on button_texts
        row = 1
        col = 0
        for text in button_texts:
            button = tk.Button(self.root, text=text, font=("Arial", 18), command=lambda t=text: self.on_button_click(t), height=2, width=5)
            button.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def create_menus(self):
        # Create menu bar
        menubar = tk.Menu(self.root)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.exit_application)
        menubar.add_cascade(label="File", menu=file_menu)

        # Add menu bar to the window
        self.root.config(menu=menubar)
        
        # Bind Ctrl+Q to Exit
        self.root.bind("<Control-q>", lambda event: self.exit_application())
    
    def on_button_click(self, char):
        if char in "0123456789":
            self.expression += char
        elif char in "+-*/":
            self.expression += f" {char} "
        elif char == "=":
            self.calculate_result()
        elif char == "C":
            self.clear()
        elif char == "sin":
            self.calculate_sin()
        elif char == "cos":
            self.calculate_cos()
        elif char == "exp":
            self.calculate_exp()

        self.update_display()

    def calculate_result(self):
        try:
            self.result = str(eval(self.expression))
            self.expression = self.result
            self.save_to_file(self.expression + " = " + self.result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid input or calculation.")
            self.expression = ""

    def calculate_sin(self):
        try:
            angle = float(self.expression)
            self.result = str(math.sin(math.radians(angle)))
            self.expression = self.result
            self.save_to_file(f"sin({angle}) = {self.result}")
        except Exception as e:
            messagebox.showerror("Error", "Invalid input for sin.")
            self.expression = ""
    
    def calculate_cos(self):
        try:
            angle = float(self.expression)
            self.result = str(math.cos(math.radians(angle)))
            self.expression = self.result
            self.save_to_file(f"cos({angle}) = {self.result}")
        except Exception as e:
            messagebox.showerror("Error", "Invalid input for cos.")
            self.expression = ""

    def calculate_exp(self):
        try:
            base = float(self.expression.split()[0])  # Assume it's the first number in the expression
            self.result = str(math.exp(base))
            self.expression = self.result
            self.save_to_file(f"exp({base}) = {self.result}")
        except Exception as e:
            messagebox.showerror("Error", "Invalid input for exp.")
            self.expression = ""

    def clear(self):
        self.expression = ""
        self.result = ""
        self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

    def save_to_file(self, text):
        with open("calculator_history.txt", "a") as file:
            file.write(text + "\n")

    def exit_application(self, event=None):
        if messagebox.askokcancel("Exit", "Do you want to exit?"):
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
