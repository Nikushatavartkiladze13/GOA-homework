# 3) შექმენით სია და for loop დახმარებით გამოიტანეთ მხოლოდ ლუწი ინდექსებზე მდგომი ელემენტები

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

for i in range(len(my_list)):
    if i % 2 == 0:
        print(i)
    else:
        continue