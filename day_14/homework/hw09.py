# დაწერეთ ისეთი პროგრამა რომელიც მომხმარებელს უპრინტავს კვირის დღეს მომხმარებლის შემოტანილი რიცხვის მიხედვით (1 არის ორშაბათი, 2 სამშაბათი და ა.შ) გამოიყენეთ if elif else


print("1. ორშაბათი")
print("2. სამშაბათი")
print("3. ოთხშაბათი")
print("4. ხუთშაბათი")
print("5. პარასკევი")
print("7. შაბათი")
print("8. კვირა")

day = input("choose day: ")

if day == "1" or day == "ორშაბათი":
    print("ორშაბათი")
elif day == "2" or day == "სამშაბათი":
    print("სამშაბათი")
elif day == "3" or day == "ოთხშაბათი":
    print("ოთხშაბათი")
elif day == "4" or day == "ხუთშაბათი":
    print("ხუთშაბათი")
elif day == "5" or day == "პარასკევს":
    print("პარასკევი")
elif day == "6" or day == "შაბათი":
    print("შაბათი")
elif day == "7" or day == "კვირა":
    print("კვირა")
else: 
    print("choose day")