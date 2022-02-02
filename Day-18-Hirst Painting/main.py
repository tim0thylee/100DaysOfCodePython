from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.penup()
screen = Screen()
screen.colormode(255)

colors = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]

x_pos = 0
y_pos = 0
tim.setposition(x_pos, y_pos)


tim.speed(10)

# Create a square
for i in range(0, 10):
    for j in range(0, 10):
        tim.dot(20, random.choice(colors))
        tim.forward(50)
    y_pos += 40
    tim.setposition(x_pos, y_pos)


# Must keep for keeping screen up.
screen.exitonclick()
