// )შექმენით ცვლადი სადაც მომხმარებელი შემოიყვანს საათს, თქვენი დავალებაა გაიგოთ ეს საათი რომელ დღის მონაკვეთს ეკუთვნის(დილა,შუადღე,საღამო,ღამე)

let userTime = Number(prompt("enter your time"))

switch(true){
    case(userTime >= 6 && userTime < 12):
        console.log("დილა")
        break
    case(userTime > 12 && userTime < 18):
        console.log("შუადღე")
        break

    case(userTime > 18 && userTime < 23):
        console.log("ღამე")
}

