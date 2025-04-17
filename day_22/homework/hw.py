# 1) შექმინთ 2 სია  , პირველი სია ინქება ცარიელი  ხოლო მეროე სია ინქება სახელებით სავსე მინიმუმ 5 , თქვენი დავალებაა ამ სიიდან  ჩაამოტომ მეორე სიაში სახელელბი რომელიც  4 სიმბოლოზე ნაკლებია


name_list = ['nika','luka','daviti','gabrieli','giorgi']
empty_list = []
for i in name_list:
    if len(i) <= 4:
        empty_list.append(i)
print(empty_list)

