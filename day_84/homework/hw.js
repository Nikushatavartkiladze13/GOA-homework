

let div = document.getElementById("div")



document.addEventListener("keydown", function(event){
    if(event.key == "ArrowRight"){
        div.style.right= "0px"
    }else if(event.key == "ArrowLeft"){
        div.style.left = "0px"
    }else if(event.key == "ArrowDown"){
        div.style.bottom = "0px"
    }else if(event.key == "ArrowUp"){
        div.style.top = "0px"
    }
})






