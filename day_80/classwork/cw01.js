// 2) დაამატეთ საიტზე ფოტო, რომელზე მაუსის გადატარებისას, უნდა შეიცვალოს ეს ფოტო. მაუსის გაწევისას კი დაუბრუნდეს ისევ საწყის ფოტოს.


let button = document.getElementById("button")
let  img = document.getElementById("img")
let button2 = document.getElementById("button2")

button.addEventListener("click", function(){
    img.src = "images/img01.png"
    img.style.width = "320px"
})

button2.addEventListener("click", function(){
    img.src = "images/img.png"
    img.style.width = "290px"
})


