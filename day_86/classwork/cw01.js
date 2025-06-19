// 1)შექმენით ცვლადი month ამ ცვლადში მომხმარებელს უნდა შემოატანინოთ თვე ოღონდ რიცხვების საშუალებით(მაგ. 1=იანვარი , 2=თებერვალი , 3 = მარტი) , ამ რიცხვების მეშვეობით დაადგინეთ რომელი თვეა და გამოსახეთ კონსოლში, ამისთვის აუცილებლად გამოიყენეთ switch , იმ შემთხვევაში თუ მომხმარებელმა შემოიყვანა სხვა სიტყვა ან 12 ზე მეტი რიცხვი console-ში გამოიტანოს რომ "ასეთი თვე არ არსებობს"



let month = prompt("enter your month (1:12)")


switch (month) {
    case "1":
        console.log("january")
        break
    case "2":
        console.log("february")
        break
    case "3":
        console.log("march")
        break
    case "4":
        console.log("april")
        break
    case "5":
        console.log("may")
        break
    case "6":
        console.log("june")
        break
    case "7":
        console.log("july")
        break
    case "8":
        console.log("august")
        break
    case "9":
        console.log("seqtember")
        break
    case "10":
        console.log("octomber")
        break
    case "11":
        console.log("november")
        break
    case "12":
        console.log("december")
        break
    default:
        console.log("ასეთი თვე არ არსებობს")
}



