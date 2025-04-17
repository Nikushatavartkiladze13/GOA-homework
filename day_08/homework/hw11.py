# შეამოწმე, არის თუ არა მომხმარებლის შემოტანილი ორი რიცხვი ერთმანეთზე მეტი და 10-ის ჯერადი.


user_number = int(input("enter your number: "))
user_number2 = int(input("enter your second number: "))
if user_number > user_number2 or user_number % 10 == 0:
    print(True)
else:
    print(False)