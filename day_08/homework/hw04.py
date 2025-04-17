
# დაწერე პროგრამა, რომელიც ამოწმებს, არის თუ არა მომხმარებლის შემოტანილი რიცხვი 100-ზე მეტი და ლუწი.


user_number = int(input("enter your number: "))

if user_number > 100 and user_number % 2 == 0:
    print(True)
else:
    print(False)