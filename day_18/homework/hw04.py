# 1-დან 100-მდე ლუწი რიცხვების ჯამი:


num = 0

for i in range(1,101):
    if i % 2 == 0:
        num += i
    else:
        continue
print(num)