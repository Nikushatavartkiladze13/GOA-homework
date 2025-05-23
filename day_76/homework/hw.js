

let h1 = document.getElementsByTagName("h1")
let sum = 0
function increase(){
    sum++
    h1[0].innerHTML = sum
    h1[0].style.color = "green"

}


function subtraction(){
    sum--
    h1[0].innerHTML = sum
    h1[0].style.color = "red"
}

function reset(){
    sum = 0
    h1[0].innerHTML = sum
    h1[0].style.color = "black"

}