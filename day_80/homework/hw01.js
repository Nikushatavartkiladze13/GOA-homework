
let img01 = document.getElementById("img")
let img02 = document.getElementById("img01")
let img03 = document.getElementById("img02")
img01.addEventListener("mouseover", function(){
    img01.src = "images/img-01.png"
})
img01.addEventListener("mouseout", function(){
    img01.src = "images/img01.png"
})



img02.addEventListener("mouseover", function(){
    img02.src = "images/img-02.png"
})
img02.addEventListener("mouseout", function(){
    img02.src = "images/img02.png"
})



img03.addEventListener("click", function(){
    img03.src = "images/img03.png"

})

img03.addEventListener("mouseout", function(){
    img03.src = "images/img04.png"
    
})