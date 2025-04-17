# შექმენით სია რომელშიც იქნება სახელები შემდეგ კი შექმენით პროგრამა რომელიც ამოშლის ყველა სახელს რომელიც "t" ასოზე იწყება და ჩაამატებს ახალ სიაში

name_list = ['tamta','tornike','giorgi','nika','daviti','luka','tamari']
t_name = []


for i in name_list:
    if i[0] == "t":
        t_name.append(i)
    else:
        continue
print(t_name)