#პრეზენტაციის თემა banki 

#creat credit card

#ვეკითხებით მომხმარებელს უნდა თ არა შექმნას საკრედითო ბარათი
print("hallo welcome to ... bank")
print("hallo user do you want make credit card")
user=input("do you?:",)
if user=="yes":
    print("ok wats your name")

#ვეკითხებით მონაცემებს
name=input("enter your name:",)
surname=input("enter your surname:",)

print("how old are you")
age=(int(input("enter your age:",)))

if age < 18:
    print("you are no't adult ")

print("enter your birtday")
yera=input("year:",)
month=input("month:",)
day=input("day:",)

#deposit
print("Hello")

#operation permition (1)
operation=input("Are you sure to perform the operation? ")
if operation=="yes":
    # money permition
    money=int(input("How much do you want to deposit in your account?: "))
    if money>0:
        # cource 
        cource=input("It's $ or lari: ")
        # cource $
        if cource=="$":
            print("Now in your account you have "+str(money)+"$")
            add=input("Do you want add another $?: ")
            # add money
            if add=="yes":
                new_deposit=int(input("Enter: "))
                print("Now you have "+str(money+new_deposit)+cource+", have a good day")
            elif add=="no":
                print("goodbay")
            else:
                print("ERROR")
        # cource lari
        elif cource=="lari":
            print("Now inn your account you have "+str(money)+"₾")
            add=input("Do you want add another ?: ")
            #add money
            if add=="yes":
                new_deposit=int(input("Enter: "))
                print("Now you have "+str(money+new_deposit)+cource+", have a good day")
            elif add=="no":
                print("goodbay")
            else:
                print("ERROR")
        else:
            print("Sorry, but you cannot deposit the amount of this course.")
    # money permition (2)
    elif money<=0:
        print("The operation cannot be performed")
    else:
        print("ERROR")
#operation permition (2)
elif operation=="no":
    print("goodbye")
else:
    print("ERROR")

#shoow balans

print("do you want to sho balsans?")
if user=="yes":
    print("ok")
if user=="no":
    print("ok bay")

def show_balance():
    print(f"your balance is {balance:.2f} lari")

balance =0

proces = True

while proces:
    print("")
    print("Hello to GOA bank:3")
    print("")
    print("BANK PROGRAM")
    print("")
    print("1.deposit")
    print("2.deposit to someone")
    print("3.show balance")
    print("4.creat credit card")
    print("5.exsit")
    print("")

    choose = input("please enter your choose: ")
if choose =="5":
    proces = False


#depoziti sxvastan

#ვეკითხებით მომხმარებელს input-ის საშვალებით  სურს თუ არა სხვასთან დეპოზიტი 
print("do you want to deposit with someone else?")
user=input("do you?:",)
if user=="yes":
    print("ok")
if user=="no":
    print("ok bay")

#ვწკითხებით ვისთან უნდა დეპოზიტის გაკეთება
name=input("persone name: ")
last_name=input("persone lastname: ")
money=float(input("How many mony do you wont to depozit: "))
if money >0:
    cource=input("lari or dolari: ")

    if cource=="lari":
        perm=input("Are you sure you want to transfer "+str(money)+" "+ "₾ "+"to "+name+" "+last_name+"? " )
        if perm=="yes":
            x=int(input("enter your card code: "))
            print("Registration completed, thanks for using")
        if perm=="no":
            print("goodbye")
    elif cource=="dolari":
        perm=input("Are you sure you want to transfer "+str(money)+" "+ "$ to"+name +" " + last_name+"? "  )
        if perm=="yes":
            x=int(input("enter your card code: "))
            print("Registration completed, thanks for using")
        if perm=="no":
            print("goodbye")
elif money <=0:
    print("ERROR")

print("Thank you for using our bank")