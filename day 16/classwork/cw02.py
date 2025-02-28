# 3) ერთიდან 100 მდე დაბეჭდეთ ყველა ლუწი რიცხვი while loop ის გამოყენებით if ების გამოყენებით


num = 1 

while num != 100:
    num += 1
    if num % 2 == 0:
        print(f"{num}. is even")
    else:
        print(f"{num}. is odd")