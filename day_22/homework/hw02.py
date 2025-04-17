# 3)  შექმენით 3 ცრილი სამივე იქნება განსხვავებული მონაცემთა ტიპიები  | ბოლეანი არა საჭირო | და შექმენით ცარიელი ცხრილი სადაც იქნება დასაწყისში ინტეჯერების ცხრილი  სტრინგების ცხრილი და მერე ფლოათების ცხრილი

my_list = ["string","nika", "GOAl-oriented academy", 5, 10, 20, 45, 12.3, 10.4,6.3]
string = []
integer = []
flt = []
for i in my_list:
    if type(i) == str:
        string.append(i)
    elif type(i) == int:
        integer.append(i)
    elif type(i) == float:
        flt.append(i)

print(flt)
print(string)
print(integer)