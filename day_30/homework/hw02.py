# შექმენით ფუნქცია რომელსაც გადაეცემა არგუმენტად რიცხვი შემდეგ კი მან უნდა დაგვიბრუნოს ლუწია ეს რიცხვი თუ კენტი

number = int(input("enter your number: "))


def even_odd(num):
    if num % 2 == 0:
        print(str(num) + " is even")
    else:
        print(str(num) + " is odd")

even_odd(number)