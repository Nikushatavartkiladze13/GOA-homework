
# შეამოწმე, არის თუ არა მომხმარებლის შემოტანილი ორი რიცხვი ერთმანეთზე მეტი და 10-ის ჯერადი.

number = int(input("enter your number: "))
num =  int(input("enter your number: "))

if number == num and number % 10 == 0 and num % 10 == 0:
    print(True)

else:
    print(False)