// 3)შექმენით სია, ამ სიაში შეინახეთ String-ტიპის მონაცემები და for-ციკლის გამოყენებით ახალ სიაში დაამატეთ ძველი სიიდან ყოველი სიტყვის პირველი ასო


let myArray = ["nika", "luka", "saba", "beka", "giorgi"]

let myString = []

for (let i of myArray){
    myString.push(i[0])
}


console.log(myString)