# დაწერე პროგრამა, რომელიც ამოწმებს, არის თუ არა რიცხვი უარყოფითი ან  ლუწი.

number = int(input("enter your number: "))


if number < 0 or number % 2 == 0:
    print(True)
else:
    print(False)