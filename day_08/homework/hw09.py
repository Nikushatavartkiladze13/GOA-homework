# დაწერე პროგრამა, რომელიც ამოწმებს, არის თუ არა რიცხვი ლუწი ან 3-ის ჯერადი.

number = int(input("enter your number: "))

if number % 3 == 0 or number % 2 == 0:
    print(True)
else:
    print(False)