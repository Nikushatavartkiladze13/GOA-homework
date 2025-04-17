# 3) ერთიდან 100 მდე დაბეჭდეთ ყველა ლუწი რიცხვი while loop ის გამოყენებით if ების გამოყენებით

first_number = 1

while first_number != 100:
    first_number += 1
    if first_number % 2 == 0:
        print(str(first_number) + " .is even")
    else:
        continue
    