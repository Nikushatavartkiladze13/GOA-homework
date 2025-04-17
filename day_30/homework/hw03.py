# შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა რიცხვი შემდეგ კი მან უნდა დაგვიბრუნოს ეს რიცხვი დადებითია თუ უარყოფითი

number = int(input("enter your number: "))


def negativ_positiv(num):
    if num < 0: 
        print(f"{num} is negativ")
    else:
        print(f"{num} is positiv")

negativ_positiv(number)