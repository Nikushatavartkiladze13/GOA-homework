let audios = [
    "Audios/crash.mp3",
    "Audios/kick-bass.mp3",
    "Audios/snare.mp3",
    "Audios/tom-1.mp3",
    "Audios/tom-2.mp3",
    "Audios/tom-3.mp3",
    "Audios/tom-4.mp3"
]
let instrumental = document.querySelectorAll(".child-div")
document.addEventListener("keyup", function(event){
        if (event.key == "w") {
        instrumental[0].style.border = "15px solid #3d465d"
    }else if (event.key == "a") {
        instrumental[1].style.border = "15px solid #3d465d"

    }else if (event.key == "s") {
        instrumental[2].style.border = "15px solid #3d465d"

    }else if (event.key == "d") {
        instrumental[3].style.border = "15px solid #3d465d"

    }else if (event.key == "j") {
        instrumental[4].style.border = "15px solid #3d465d"

    }else if (event.key == "k") {
        instrumental[5].style.border = "15px solid #3d465d"

    }else if (event.key == "i") {
        instrumental[6].style.border = "15px solid #3d465d"

    }
})
document.addEventListener("keydown", function (event) {
    if (event.key == "w") {
        let idk = new Audio(audios[0])
        idk.play()
        instrumental[0].style.border = "10px solid #53607c"
    }else if (event.key == "a") {
        let idk = new Audio(audios[1])
        idk.play()
        instrumental[1].style.border = "10px solid #53607c"

    }else if (event.key == "s") {
        let idk = new Audio(audios[2])
        idk.play()
        instrumental[2].style.border = "10px solid #53607c"

    }else if (event.key == "d") {
        let idk = new Audio(audios[3])
        idk.play()
        instrumental[3].style.border = "10px solid #53607c"

    }else if (event.key == "j") {
        let idk = new Audio(audios[4])
        idk.play()
        instrumental[4].style.border = "10px solid #53607c"

    }else if (event.key == "k") {
        let idk = new Audio(audios[5])
        idk.play()
        instrumental[5].style.border = "10px solid #53607c"

    }else if (event.key == "i") {
        let idk = new Audio(audios[6])
        idk.play()
        instrumental[6].style.border = "10px solid #53607c"

    }
})
