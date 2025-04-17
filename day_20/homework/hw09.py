
#10) დაითვალე დადებითი და უარყოფითი რიცხვების ჯამი სიიდან
numbers = [4, -7, 3, -2, 8, -5, 6, -1]


positive_sum = 0
negative_sum = 0


for i in range(len(numbers)):
    if numbers[i] > 0:
        positive_sum += numbers[i]
    elif numbers[i] < 0:
        negative_sum += numbers[i]

print(positive_sum)
print(negative_sum)
