
let img01 = document.getElementById("image-1")
let img02 = document.getElementById("image-2")

img01.addEventListener("mouseover", function(){
    img01.src = "images/img-01.png"
})
img01.addEventListener("mouseout", function(){
    img01.src = "images/img01.png"
})


img02.addEventListener("mouseover", function(){
    img02.src = "images/img-02.png"

})

img02.addEventListener("click", function(){
    img02.src= "images/img02.png"
})

img02.addEventListener("mouseout", function(){
    img02.src= "images/img02.png"
})