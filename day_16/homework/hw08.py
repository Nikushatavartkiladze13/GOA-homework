# 9) დაბეჭდეთ 20 დან 70 მდე ყველა 3ის ჯერადი რიცხვები while loop ის გამოყენებით

number = 20 

while number != 70:
    number += 1
    if number % 3 == 0:
        print(number)
    else:
        continue