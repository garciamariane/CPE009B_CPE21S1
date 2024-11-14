import tkinter as tk
from tkinter import messagebox
import math

# Functions for calculation
def add():
    try:
        result.set(float(entry1.get()) + float(entry2.get()))
        add_to_history(f"{entry1.get()} + {entry2.get()} = {result.get()}")
    except ValueError:
        show_error("Please enter valid numbers.")

def subtract():
    try:
        result.set(float(entry1.get()) - float(entry2.get()))
        add_to_history(f"{entry1.get()} - {entry2.get()} = {result.get()}")
    except ValueError:
        show_error("Please enter valid numbers.")

def multiply():
    try:
        result.set(float(entry1.get()) * float(entry2.get()))
        add_to_history(f"{entry1.get()} * {entry2.get()} = {result.get()}")
    except ValueError:
        show_error("Please enter valid numbers.")

def divide():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 != 0:
            result.set(num1 / num2)
            add_to_history(f"{num1} / {num2} = {result.get()}")
        else:
            show_error("Error! Division by zero.")
    except ValueError:
        show_error("Please enter valid numbers.")

def square_root():
    try:
        num = float(entry1.get())
        if num >= 0:
            result.set(math.sqrt(num))
            add_to_history(f"√{num} = {result.get()}")
        else:
            show_error("Cannot calculate square root of negative numbers.")
    except ValueError:
        show_error("Please enter a valid number.")

def power():
    try:
        base = float(entry1.get())
        exponent = float(entry2.get())
        result.set(math.pow(base, exponent))
        add_to_history(f"{base} ^ {exponent} = {result.get()}")
    except ValueError:
        show_error("Please enter valid numbers.")

def sine():
    try:
        angle = math.radians(float(entry1.get()))  # Convert to radians
        result.set(math.sin(angle))
        add_to_history(f"sin({entry1.get()}) = {result.get()}")
    except ValueError:
        show_error("Please enter a valid number.")

def cosine():
    try:
        angle = math.radians(float(entry1.get()))  # Convert to radians
        result.set(math.cos(angle))
        add_to_history(f"cos({entry1.get()}) = {result.get()}")
    except ValueError:
        show_error("Please enter a valid number.")

# History to display operations performed
history = []

def add_to_history(operation):
    history.append(operation)
    if len(history) > 5:  # Keep only the last 5 operations
        history.pop(0)
    history_label.config(text="\n".join(history))

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result.set("")
    history.clear()
    history_label.config(text="History:")

def show_error(message):
    messagebox.showerror("Input Error", message)

# Create the main window
root = tk.Tk()
root.title("Group 3 Activity 7 - suplementary activity")

# Create StringVar to hold the result
result = tk.StringVar()

# Styling: Set background color for the window
root.config(bg="#f4f4f4")  # Light gray background

# Create the layout
tk.Label(root, text="Enter first number:", bg="#f4f4f4", font=("Georgia", 12)).grid(row=0, column=0, sticky="w", padx=10, pady=5)
entry1 = tk.Entry(root, bg="#e0e0e0", fg="black", font=("Georgia", 12))
entry1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Enter second number:", bg="#f4f4f4", font=("Georgia"   , 12)).grid(row=1, column=0, sticky="w", padx=10, pady=5)
entry2 = tk.Entry(root, bg="#e0e0e0", fg="black", font=("Arial", 12))
entry2.grid(row=1, column=1, padx=10, pady=5)

# Buttons for operations (with background color)
tk.Button(root, text="Add", command=add, width=10, bg="#4CAF50", fg="white", font=("Georgia", 12)).grid(row=2, column=0, padx=10, pady=5)
tk.Button(root, text="Subtract", command=subtract, width=10, bg="#f44336", fg="white", font=("Georgia", 12)).grid(row=2, column=1, padx=10, pady=5)
tk.Button(root, text="Multiply", command=multiply, width=10, bg="#2196F3", fg="white", font=("Georgia", 12)).grid(row=3, column=0, padx=10, pady=5)
tk.Button(root, text="Divide", command=divide, width=10, bg="#FF9800", fg="white", font=("Georgia", 12)).grid(row=3, column=1, padx=10, pady=5)
tk.Button(root, text="Square Root", command=square_root, width=10, bg="#9C27B0", fg="white", font=("Georgia", 12)).grid(row=4, column=0, padx=10, pady=5)
tk.Button(root, text="Power", command=power, width=10, bg="#3F51B5", fg="white", font=("Georgia", 12)).grid(row=4, column=1, padx=10, pady=5)
tk.Button(root, text="Sine", command=sine, width=10, bg="#00BCD4", fg="white", font=("Georgia", 12)).grid(row=5, column=0, padx=10, pady=5)
tk.Button(root, text="Cosine", command=cosine, width=10, bg="#8BC34A", fg="white", font=("Georgia", 12)).grid(row=5, column=1, padx=10, pady=5)

# Clear button (with different style)
tk.Button(root, text="Clear", command=clear, width=20, bg="#607D8B", fg="white", font=("Georgia", 12)).grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Label to show result (with background color)
tk.Label(root, text="Result:", bg="#f4f4f4", font=("Georgia", 12)).grid(row=7, column=0, sticky="w", padx=10, pady=5)
result_label = tk.Label(root, textvariable=result, bg="#f4f4f4", font=("Georgia", 14, "bold"), fg="green")
result_label.grid(row=7, column=1, padx=10, pady=5)

# History Label (with styling)
history_label = tk.Label(root, text="History:", anchor="w", justify="left", bg="#f4f4f4", font=("Georgia", 10))
history_label.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

# Start the main loop
root.mainloop()
