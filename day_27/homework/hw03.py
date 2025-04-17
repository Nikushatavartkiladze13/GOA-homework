# 4) დაწერეთ ალგორითმი, რომელიც მომხმარებელს შეეკითხება რიცხვს. თუ რიცხვი ლუწია გაყავით ორზე, სხვა შემთხვევაში გაამრავლეთ სამზე და მიუმატეთ ერთი.


user_number = int(input("enter your number: "))


if user_number % 2 == 0:
    print(user_number // 2)
else:
    print(user_number * 3 + 1)