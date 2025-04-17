# 2) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი მომხმარებლის შემოტანილ რიცვამდე დაბეჭდეთ ყველა ლუწი რიცხვი


user_number = int(input("enter your number: "))


for i in range(1, user_number):
    if i % 2 == 0:
        print(i)
    else:
        continue