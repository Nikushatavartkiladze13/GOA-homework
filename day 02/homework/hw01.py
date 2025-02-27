from turtle import*


width(7)
speed(0)

for _ in range(4):
    forward(300)
    left(90)

penup()
goto(63, 0)
pendown()

color("black")
begin_fill()
left(90)
forward(40)

for _ in range(9):
    forward(30)
    right(20)

forward(70)

end_fill()

penup()
goto(0, 300)
pendown()

left(180)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
left(90)
forward(24)

for _ in range(4):
    left(90)
    forward(30)
    right(90)
    forward(30)
    right(90)
    forward(30)
    left(90)
    forward(24)
    
left(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
left(90)

left(90)
forward(90)
right(90)
forward(80)
right(90)
forward(390)

right(90)
forward(80)


penup()
goto(0, 300)
pendown()

right(90)
forward(90)
left(90)
forward(80)
left(90)
forward(390)
left(90)
forward(80)


penup()
goto(55, 300)
pendown()
color("black")
left(90)

forward(100)
right(90)


forward(190)
right(90)
forward(100)
right(90)



penup()
goto(40, 170)
pendown()
color("brown")
begin_fill()
right(90)
forward(90)
for _ in range(10):
    right(16)
    forward(5)

right(20)
forward(90)

right(90)
forward(30)


penup()
goto(260, 170)
pendown()

right(90)
forward(90)
for _ in range(10):
    left(16)
    forward(5)

left(20)
forward(90)

left(90)
forward(30)
end_fill()
exitonclick()