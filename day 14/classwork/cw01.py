# 2) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი მომხმარებლის შემოტანილ რიცვამდე დაბეჭდეთ ყველა ლუწი რიცხვი


user_num = int(input("enter your number: "))

for i in range(1, user_num):
    if i % 2 == 0:
        print(f"{i}. even")
    else:
        continue