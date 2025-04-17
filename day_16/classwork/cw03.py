#4) ერთიდან 100 მდე დაბეჭდეთ ყველა რიცხვი თან გვერძე მიუწერეთ ლუწია თუ კენტი  while loop ის გამოყენებით 

number = 1

while number != 100:
    number += 1
    if number % 2 == 0:
        print(str(number) + " .Is Even")
    else:
        print(str(number) + " .Is Odd")