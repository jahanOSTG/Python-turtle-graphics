import turtle  
# Creating turtle  
t = turtle.Turtle()  
  
turtle.bgcolor("black")  
turtle.pensize(1)  
turtle.speed(0)  
  
  
for i in range(19):  
        for colors in ["yellow","white"]:  
            turtle.color(colors)  
            turtle.circle(100)  
            turtle.left(10)  
  
  
turtle.hideturtle()  
turtle.mainloop()  