# დაწერე პროგრამა, რომელიც ამოწმებს, არის თუ არა რიცხვი ერთდროულად 50-ზე ნაკლები და 10-ის ჯერადი.

user_number = int(input("enter your number: "))


if user_number < 50 and user_number % 10 == 0:
    print(True)
else:
    print(False)