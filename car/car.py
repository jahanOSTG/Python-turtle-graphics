import turtle

def draw_rectangle(color, x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

def draw_circle(color, x, y, radius):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_text(text, x, y, font_size=10, color="white"):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.write(text, font=("Italic", font_size, "bold"))

def draw_car():
    turtle.speed(4)
    
    # Draw the car body (multicolored)
    draw_rectangle("royalblue", -100, 0, 200, 50)  # Main body
    draw_rectangle("red", -100, 0, 20, 40)  # Side stripe
    draw_rectangle("yellow", 80, 0, 20, 40)  # Other side stripe
    
    # Draw the top part of the car
    draw_rectangle("deepskyblue", -60, 50, 120, 40)

    # Draw the windows (gradient effect)
    draw_rectangle("lightgray", -55, 55, 40, 30)
    draw_rectangle("white", 15, 55, 40, 30)

    # Draw the headlights and backlights
    draw_rectangle("red", 95, 10, 10, 10)  # Front light
    draw_rectangle("yellow", -105, 10, 10, 10)  # Rear light

    # Draw the wheels (colorful wheels)
    draw_circle("black", -60, -10, 20)
    draw_circle("black", 60, -10, 20)
    draw_circle("white", -60, -10, 10) 
    draw_circle("white", 60, -10, 10)  
    draw_circle("black", -60, -10, 5)
    draw_circle("black", 60, -10, 5)

    # Add "Richmond" on the car
    draw_text("Richmond", -50, 20, 10, "Pink")

    turtle.hideturtle()
    turtle.done()

draw_car()
