# 3) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი მომხარებლის შემოტანილ რიცხვამდე დაბეჭდეთ ყველა რიცხვის საშუალო არითმეტიკული

user_num = int(input("enter your number: "))
num = 0

for i in range(1, user_num):
    num += i
number = num // user_num
print(number)