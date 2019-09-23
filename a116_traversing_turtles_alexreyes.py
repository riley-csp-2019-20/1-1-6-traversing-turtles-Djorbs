#   a116_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
    t = trtl.Turtle(shape=s)
    my_turtles.append(t)

#  Tells where the turtle should start
startx = 0
starty = 0
direction = 180

# Calls the turtles and moves them
for t in my_turtles:
    new_color = turtle_colors.pop()
    t.pencolor(new_color)
    t.fillcolor(new_color)
    t.penup()
    t.goto(startx, starty)
    t.pendown()
    t.setheading(direction)
    t.right(93)     
    t.forward(50)
    direction = t.heading()
    #	Gives a new position for each turtle
    startx = t.xcor()
    starty = t.ycor()


wn = trtl.Screen()
wn.mainloop()