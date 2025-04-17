#  3) პითონში turtle ის გამოყენებით ააგეთ სასახლე რაც შეიძლება დახვეწილი და ლამაზი ვნახოთ როგორი გამოგივათ
from turtle import *

# we want to paint palace
#step 1: draw square
speed(30)
width(7)
color("black")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

right(180)
forward(100)

right(90)
forward(250)

right(90)
forward(100)

right(90)
forward(50)

penup()
goto(200,200)
pendown()

right(180)
forward(50)

right(90)
forward(100)

right(90)
forward(250)

right(90)
forward(100)

right(90)
forward(200)

left(90)
forward(50)

right(90)
forward(80)

left(90)
forward(100)

left(90)
forward(80)
#end a spuare

# we want to paint a roof 
color("red")
penup()
goto(300,250)
pendown()

right(135)
forward(70)

left(90)
forward(70)


penup()
goto(150,280)
pendown()

right(85)
forward(70)

left(85)
forward(70)

penup()
goto(0,250)
pendown()

right(90)
forward(70)

left(90)
forward(70)
#end a roof

#we want to paint a door
color("brown")

penup()
goto(50,0)
pendown()

right(135)
forward(100)

right(90)
forward(100)
right(90)
forward(100)
#end a door

#we want to paint a window


penup()
goto(220,200)
pendown()
color("grey")

forward(50)
left(90)

forward(50)
left(90)

forward(50)
left(90)

forward(50)

penup()
goto(-30,200)
pendown()

left(90)
forward(50)

right(90)
forward(50)

right(90)
forward(50)

right(90)
forward(50)


exitonclick()
