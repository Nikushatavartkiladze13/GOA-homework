#  შექმენით პროგრამა რომელიც დაითვლის სიაში რამდენჯერ მეორდება თქვენი სახელი არ გამოიყენოთ count ფუნქცია 


name = ["nika","luka","daviti","nika","giorgi","makvala","svarchika genadi","nika"]
my_name = []

for i in name:
    if i == "nika":
        my_name.append(i)
    else:
        continue

print(len(my_name))
       