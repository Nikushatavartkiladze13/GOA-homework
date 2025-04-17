# 1) შექმენით კალკულატორი, მომხმარებელს შეეკითხეთ ორი რიცხვი, შემდეგ შეეკითხეთ რა მოქმედების შესრულება სურს ამ ორ რიცხვზე და მისი პასუხიდან გამომდინარე შეასრულეთ მოქმედება და დაბეჭდეთ მაგალითად თუ მომხმარებელი შემოიტანს რიცხვებს 5 და 7 , და შემოიტანს მოქმედებას მაგალითად დამატებას თქვენ უნდა დაუბეჭდოთ 5 + 7 = 12

user_number = int(input("enter your number: "))
user_number2 = int(input("enter your number: "))
print("1. +")
print("2. -")
print("3. *")
print("4. /")

task = input("choose a task: ")

if task == "+" or task == "1":
    sum = user_number + user_number2
    print(f"{user_number} + {user_number2} = {sum}")
elif task == "-" or task == "2":
    sum_2 = user_number - user_number2 
    print(f"{user_number} - {user_number2} = {sum_2}")
elif task == "*" or task == "3":
    sum_3 = user_number * user_number2
    print(f"{user_number} * {user_number2} = {sum_3}")
elif task == "/" or task == "4":
    sum_4 = user_number / user_number2
    print(f"{user_number} / {user_number2} = {sum_4}")

else:
    print("choose a task ")


























