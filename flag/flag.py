from turtle import *

#background
speed(1)
setup(600, 280) 
bgcolor("seagreen")


penup()
goto(-50, -50)  
pendown()

# Draw the red circle
color("red")
begin_fill()
circle(80)  #radius
end_fill()  

hideturtle()
done()
