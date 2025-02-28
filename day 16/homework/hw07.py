# 8) დაბეჭდეთ 50 დან 100 მდე ყველა 5ის ჯერადი რიცხვები while loop ის გამოყენებით


num = 50

while num != 100:
    num += 1 
    if num % 5 == 0:
        print(num)
    else:
        continue