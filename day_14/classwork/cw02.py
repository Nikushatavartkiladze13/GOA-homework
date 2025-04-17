#      3) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი მომხარებლის შემოტანილ რიცხვამდე დაბეჭდეთ ყველა რიცხვის საშუალო არითმეტიკული 



user_number = int(input("enter your number: "))

num = 0

for i in range(1, user_number):
    num += i
number = num // user_number

print(number)