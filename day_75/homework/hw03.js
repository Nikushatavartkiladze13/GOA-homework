// 3) შექმენით ობიექტი user , ამ ობიექტში შეინახე შესაბამისი key-ები , for in - ციკლის  გამოყენებით გადაუარე თითოეულ key-ს და გამოსახე console-ში

let user = {
    userName : "nika",
    userSurname : "tavartkiladze",
    age: 16,
    live: "khulo",
    hobby : "basketball"
}


for (let i in user){
    console.log(i + " is " + user[i])
}