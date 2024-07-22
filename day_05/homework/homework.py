# უნდა დახაზოთ სასახლე turtle ის გამოყენებით და თქვენი გემოვნებით გააფორმოთ 
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
# გააკეთეთ 3 ცალი სწორი კოდი და 3 ცალი არასწორი კოდი და უნდა ახსნათ რატომ არის ეს კოდი სწორი და რატომ არის ეს კოდი არასწორი
 # სწორი
print("hello world")
print("my name is Nika")
print("may favorite car is BMW")

# არასწორი
# print(name) # არსწორია იმიტომ, რომ აკლია ბრჭყალები
# print(("hello Nika")) # არსწორია იმიტომ, რომ უნდა ჰქონდეს მხოლოდ ორი ფრიჩხილი
# print My surname is Tavartkiladze # არსწორია იმიტომ, რომ  აკლია ფრჩხილები და ბრჭყალები

# ახსენით debugger-ი რაარის კომენტარებით და გააკეთეთ ასევე მაგალითებიც


# debbuger -არის გამართვის პროგრამა, გასამართი/გამმართველი პროგრამა (დამხმარე პროგრამა, რომელიც გამოიყენება სხვა პროგრამების შესამოსწმებლად გასამართად)
 


# შექმენით ცვლადი რომელიც იქნება name და მინიჭებული იქნება თქვენი სახელი და უნდა დაპრინტოთ ეს ცვლადი სწორი გზით და არასწორი გზით და უნდა ახსნათ კომენტარებით რატომ არის ეს გზა სწორი და რატომ არ არის ეს გზა სწორი

#name = "Nika Tavarkiladze"

#print(name)
print("name") #არასწორია იმიტომ რომ ცვლადის სახელს არ სჭირდება ბრჭყალები ბრჭყალებით, კი გამოვა იგივე სახელი რასაც ბრჭყალებში მოვაქცევთ

# დაპრინტეთ GOA is the best academy in georgia სწორი გზით და არასწორი გზით და ახსენით კომენტარებით რატომ არის ეკ გზა სწორი და რატომ არ არის მეორე გზა სწორი
 
print("GOA is the best academy in geogia")
# print"Goa is the best academy in geogia" არასწორია იმიტომ რომ აკლია ბრჩხილები
