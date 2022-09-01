
from turtle import * 
#we want to paint house   
speed(10)
shape("turtle")
width(7)

color ("red")

forward (200)
left(90)
forward (200)
left(90)
forward (200)
left(90)
forward (200)
left(90)
             #make door
begin_fill()             
forward(70)   
color("black")
left(90)
forward(100)
right(90)
forward(60)
right(90)
forward(100)
end_fill()
penup()


               #make a roof
goto(200,200)
pendown()
color("sienna")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
penup()
end_fill()

#make windows
begin_fill()
goto(0, 180)
pendown()
color("black")
left(120)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()
penup()



goto(200, 180)
pendown()
begin_fill()
color("black")
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()





exitonclick()
