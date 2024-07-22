# 1) sololearn module 3 quiz ის ჩათვლით
 

#  2) შექმენით დროში მოგზაურობის პროგრამა, რომელიც მომხმარებელს შეეკითხება მის ამჟამინდელ ასაკს, ამჟამინდელ წელს, რამდენი წლით სურს დროში მოგზაურობა, შემდეგ კი პროგრამა დაბეჭდავს დროში მოგზაურობის შემდეგ რომელი წელი იქნება და რამდენი წლის იქნება მომხმარებელი დროში მოგზაურობის შემდეგ

age = int(input("How old are you?: "))
year = int(input("What year is it?: "))
travel_time = int(input("How many years do you want to travel back in time?: "))


new_age = age + travel_time

print(f"After time travel from {year}, you will be {new_age} years old")
