# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.

#Area = πr^2
#Circumference = 2πr
from tkinter import messagebox,simpledialog,Tk,Canvas
import tkinter as tk

if __name__ == '__main__':
#ask user if they would calculate the area of the circle
 v=simpledialog.askstring(title=None, Prompt="Would you like to calculate the area of the circle")
