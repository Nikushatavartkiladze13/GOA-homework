// 5)შექმნილ ობიექტს გადაუარეთ for ციკლით და გამოიტანეთ key და value შემდეგი ფორმატით: "{key} is {value}"



let myInfo = {
    name : "nika",
    surname : "tavartkiladze",
    age: 16,
}



for(let i in myInfo){
    console.log(i + " is " + myInfo[i])
}
