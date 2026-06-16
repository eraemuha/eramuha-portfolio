## Import the turtle module.
import turtle

## Create a new turtle named amy.
amy = turtle.Turtle()

## Set amy's color.
turtle_color = "lightblue"
turtle_distance = 100
turtle_angle = 90
amy.color(turtle_color)

## Have amy draw a square
for sides in [1, 2, 3, 4]:
    amy.forward(turtle_distance)
    amy.right(turtle_angle)


builder = turtle.Turtle()
builder.color("red")
builder.width(5)

angles = [-90, 0, 0, -90,
          135, 0, 0, 0, 
          90, 0, 0, 0,
          135, -90, 0, 0,
          90, 0, 0, 0]

for angle in angles:
    builder.right(angle)
    builder.forward(25)

# Loops inside loops
for side in [1, 2, 3, 4]:
    builder.forward(100)
    builder.right(90)
    for side in [1, 2, 3, 4]:
        builder.forward(10)
        builder.right(90)


amy = turtle.Turtle()

## Make the width thicker so that the line will be easier to see
amy.width(5)

## Move back without drawing anything
amy.penup()
amy.back(140)
amy.pendown()

## Draw three shapes of different colors, with space in between
for prettycolor in ["red", "orange", "yellow"]:
    amy.color(prettycolor)
    for side in [1, 2, 3, 4]:
        amy.forward(50)
        amy.right(90)
    amy.penup()
    amy.forward(100)
    amy.pendown()