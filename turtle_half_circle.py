import turtle
t = turtle.Turtle()

t.pencolor("black")  # Set pen color properly
t.fillcolor("blue")  # Set fill color

t.begin_fill()
t.circle(100, 200)  # Draws a circle with 100-degree arc
t.end_fill()

turtle.done()  # Keeps the window open
