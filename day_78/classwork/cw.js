// შექმენით დოკუმენტში რამდენიმე ერთნაირი ელემენტი და querySelector()ის და  querySelectorAll() ის გამოყენებით javascript-იდან შეუცვალეთ სტილები


let h1 = document.querySelector("h1")
let h2 = document.querySelectorAll("h1")

h1.style.color = "green"
h1.style.fontSize = "900"

h2[1].style.color = "red"
h2[2].style.color = "blue"

