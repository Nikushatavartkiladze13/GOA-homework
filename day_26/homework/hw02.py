#  შექმენით სია რომელშიც იქნება რენდომ რიცხვები მოთავსებული შემდეგ კი შექმენით მეორე სია რომელშიც გადაიტანთ პირველი სიიდან მხოლოდ ლუწ რიცხვებს

number_list = [12,23,75,13,32,10,9,4,2,8,7,50,31,65,53,62]
even_number = []


for i in number_list:
    if i % 2 == 0:
        even_number.append(i)
    else:
        continue
print(even_number)