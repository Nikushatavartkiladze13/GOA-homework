# შექმენით სია რომელშიც იქნება მოთავსებული რენდომ რიცხვები შემდეგ კი ამ სიიდან ამოშალეთ ყველა ლუწი რიცხვი

number_list = [12,23,75,13,32,10,9,4,2,8,7,50,31,65,53,62]

for i in number_list:
    if i % 2 == 0:
        number_list.remove(i)
    else:
        continue
print(number_list)