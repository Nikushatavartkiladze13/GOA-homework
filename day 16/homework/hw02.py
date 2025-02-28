#  3) დაბეჭდეთ 1 დან 50 მდე მხოლოდ კენტი რიცხვები if else ის გამოყენების გარეშე

num = 1

while num != 50:
    num += 1
    if num % 2 == 0 :
        print(f"{num}. is even ")
    else:
        print(f"{num}. is odd")