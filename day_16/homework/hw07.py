#  8) დაბეჭდეთ 50 დან 100 მდე ყველა 5ის ჯერადი რიცხვები while loop ის გამოყენებით


number = 50

while number != 100:
    number += 1
    if number % 5 == 0:
        print(number)
    else:
        continue