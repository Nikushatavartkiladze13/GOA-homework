from turtle import *


#we want to paint a house

#step 1: draw square
speed(30)
width(7)
color("green")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)



#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end of roof

#drawing a window
color("orange")
begin_fill()
left(120)
forward(70)
right(90)

forward(60)
right(90)

forward(70)
right(90)

forward(60)
end_fill() 

penup()
goto(200,200)
pendown()


color("orange")
begin_fill()
left(90)
forward(70)

left(90)
forward(60)

left(90)
forward(70)

left(90)
forward(60)
end_fill()

color("black")
penup()
goto(165,200)
pendown()

left(180)
forward(60)

penup()
goto(200,170)
pendown()

right(90)
forward(70)

color("black")
penup()
goto(35,200)
pendown()

left(90)
forward(60)

color("black")
penup()
goto(70,170)
pendown()

right(90)
forward(70)

exitonclick()