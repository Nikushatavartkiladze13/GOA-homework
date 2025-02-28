#  10) დაბეჭდეთ 1 დან 100 მდე დაბეჭდეთ მხოლოდ ის რიცხვები რომლებიც 3 ჯერადიც არის და 5 ჯერადიც


num = 1

while num != 100:
    num += 1
    if num % 3 == 0 and num % 5 == 0:
        print(num)
    else:
        continue