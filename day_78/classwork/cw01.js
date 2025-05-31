// 2)createElement-ის გამოყენებით შექმენით ერთი მშობელი div-ელემენტი, ეს div-ი ჩაამატეთ body-ში , შემდეგ ამ მშობელ div-ში ჩაამატეთ კიდევ ორი შვილი div-ი და განალაგეთ ვერტიკალურად ერთმანეთისგან თანაბარი დაშორებით ,  პირველი დივი იყოს წითელი მეორე იყოს მწვანე , ასევე დაუმატეთ სასურველი სტილები 


let body = document.body

let div = document.createElement("div")
body.style.display = "flex"
body.style.justifyContent = "center"
body.style.alignItems = "center"
body.style.height = "100vh"

body.appendChild(div)

div.style.display = "flex"
div.style.justifyContent = "center"
div.style.alignItems = "center"
div.style.flexDirection = "column"
div.style.gap = "20px"
div.style.width = "300px"
div.style.height = "300px"
div.style.backgroundColor = "green"

let childDiv = document.createElement("div")
let childDiv2 = document.createElement("div")

div.appendChild(childDiv)

div.appendChild(childDiv2)


childDiv.style.width = "100px"
childDiv.style.height = "100px"
childDiv.style.backgroundColor = "red"

childDiv2.style.width = "100px"
childDiv2.style.height = "100px"
childDiv2.style.backgroundColor = "blue"
