# Random turtle
# Import statement
import turtle
import random

# Assignment statement
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

pyart = turtle.Turtle()
pyart.width(20)

# Compund statement
for step in range(100):
    # Change this to use a random number.
    angle = random.randint(-90,90)

    # Change this to use a random color.
    color = random.choice(colors)

    pyart.color(color)
    pyart.right(angle)
    pyart.forward(10)