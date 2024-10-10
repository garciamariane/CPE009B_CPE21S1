from tkinter import *

class MyWindow:
    def __init__(self, window):
        self.lb1 = Label(window, fg="Red", font="Georgia", text = " SIMPLE CALCULATOR")
        self.lb1.place(x=100, y=50)

        self.lb2 = Label(window, fg="green", font="Georgia", text="Number 1:")
        self.lb2.place(x=70, y=80)
        self.t2 = Entry(window, bd=2)
        self.t2.place(x=150, y=80)

        self.lb3 = Label(window, fg="green", font="Georgia", text="Number 2:")
        self.lb3.place(x=70, y=110)
        self.t3 = Entry(window, bd=2)
        self.t3.place(x=150, y=110)

        self.lb4 = Label(window, fg="green", font="Georgia", text="Answer:")
        self.lb4.place(x=70, y=140)
        self.t4 = Entry(window, bd=2)
        self.t4.place(x=150, y=140)

        # Button for Addition (renamed to btn1)
        self.btn1 = Button(window, text="ADD", command=self.add)
        self.btn1.place(x=50, y=170)

        # Button for Subtraction (renamed to btn2)
        self.btn2 = Button(window, text="SUBTRACT", command=self.subtract)
        self.btn2.place(x=100, y=170)

        self.btn3 = Button(window, text= "DIVIDE", command= self.divide )
        self.btn3.place(x= 180, y=170)

        self.btn4 = Button(window, text= "MUlTIPLY", command=self.multiply)
        self.btn4.place(x=250, y=170)


    def add(self):
        try:
            # Retrieve the values from the entry fields
            num1 = float(self.t2.get())
            num2 = float(self.t3.get())

            # Perform the addition
            result = num1 + num2

            # Display the result in the t4 entry field
            self.t4.delete(0, END)
            self.t4.insert(0, str(result))

        except ValueError:
            # Handle cases where the input is not a valid number
            self.t4.delete(0, END)
            self.t4.insert(0, "Invalid input")

    def subtract(self):
        try:
            # Retrieve the values from the entry fields
            num1 = float(self.t2.get())
            num2 = float(self.t3.get())

            # Perform the subtraction
            result = num1 - num2

            # Display the result in the t4 entry field
            self.t4.delete(0, END)
            self.t4.insert(0, str(result))

        except ValueError:
            # Handle cases where the input is not a valid number
            self.t4.delete(0, END)
            self.t4.insert(0, "Invalid input")

#iivbfvbsvhfbhbvhfbvfhvbfhvbfdhvjbfdjvbfvbfdjhbdhvgwuygwILesicufnhcufief

    def divide (self):
        try:
            # Retrieve the values from the entry fields
            num1 = float(self.t2.get())
            num2 = float(self.t3.get())

            # Perform the subtraction
            result = num1/num2

            # Display the result in the t4 entry field
            self.t4.delete(0, END)
            self.t4.insert(0, str(result))

        except ValueError:
            # Handle cases where the input is not a valid number
            self.t4.delete(0, END)
            self.t4.insert(0, "Invalid input")

#kdshdsffvbgbfggsfgdsjgfkgfksgfskjhghfghfdgjhdfgjfhgjdhgfkjhg

    def multiply (self):
        try:
            # Retrieve the values from the entry fields
            num1 = float(self.t2.get())
            num2 = float(self.t3.get())


            result = num1 * num2


            self.t4.delete(0, END)
            self.t4.insert(0, str(result))

        except ValueError:
            self.t4.delete(0, END)
            self.t4.insert(0, "Invalid input")



window = Tk()
mywin = MyWindow(window)
window.geometry("400x300+10+10")
window.title("Simple Calculator")
window.mainloop()
