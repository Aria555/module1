import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    j=turtle.Turtle()
    # Ask the user what shape they want to draw and store it in a variable
    shape=simpledialog.askstring(title=None, prompt="what shape would you like to draw")
    if(shape=="circle"):
        j.begin_fill()
        j.circle(20, steps=30)
        j.end_fill()
    elif(shape=="square"):
        j.forward(100)
        j.left(90)
        j.forward(100)
        j.left(90)
        j.forward(100)
        j.left(90)
        j.forward(100)
        j.left(90)
    elif(shape=="triangle"):
        for i in range(3):
            j.forward (80)
            j.right(60)
            j.goto(10,10)
    # Draw the shape requested by the user using if-elif-else statements
    else:
        messagebox.showinfo(message="shape not available")

    # Call the turtle .done() method
