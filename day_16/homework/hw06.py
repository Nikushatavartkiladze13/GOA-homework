#  7) დაბეჭდეთ 100 დან 200 მდე ყველა რიცხვი გვერძე კი მიუწერეთ ლუწია თუ კენტი გამოიყენეთ while loop და if else


number = 100

while number != 200:
    number += 1
    if number % 2 == 0:
        print(str(number) + " .Is Even")
    else:
        print(str(number) + " .Is Odd")