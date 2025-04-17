# მომხმარებლის შემოტანილი რიცხვი შეამოწმე, არის თუ არა  20-ის ჯერადი და დადებითი.

user_number = int(input("enter your number: "))


if user_number % 20 == 0 and user_number > 0:
    print(True)
else:
    print(False)