# 3) მომხმარებელს შემოატანინეთ ორი რიცხვი ხოლო ამის შემდეგ for loop - ის გამოყენებით გამოიტანეთ ამ რიცხვებს შორის ჯამი და ნამრავლი

user_number1 = int(input("enter your first number: "))
user_number_2 = int(input("enter your second number: "))


for i in range(user_number1, user_number_2 + 1):
    user_number1 += i
    user_number_2 *= i

print(user_number_2)
print(user_number1)