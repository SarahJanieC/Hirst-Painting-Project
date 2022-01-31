
# Hirst Painting Project written in Python that utilizes the Turtle Module/GUI to 

import turtle as t
import random

t.colormode(255)
t.speed("fastest")
t.penup()
t.hideturtle()
# get random colors
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# generate color list
color_list = []
for i in range(0, 30):
    color_list.insert(i, random_color())

t.setheading(225)
t.forward(250)
t.setheading(0)
num_of_dots = 101

for i in range(1, num_of_dots):
    t.dot(20, random.choice(color_list))
    t.forward(50)

    if(i % 10 == 0):
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)


screen = t.Screen()
screen.title("Hirst Painting")
screen.exitonclick()