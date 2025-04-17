# 4) დაბეჭდეთ 1-დან 49-მდე ყველა კენტი რიცხვი


for i in range(1, 50):
    if i % 2 == 0:
        continue
    else:
        print(i)