# შეამოწმე მომხმარებლის შემოტანილი რიცხვი თუ არის 5-ის ან 10-ის ჯერადი.


user_number = int(input("enter your number: "))


if user_number % 5 == 0 or user_number % 10 == 0:
    print(True)
else:
    print(False)