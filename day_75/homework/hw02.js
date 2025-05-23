// 2)არსებულ car ობიექტს , ობიექტის გარედან დაამატეთ color  და price  , ასევე ამოშალეთ milage , შემდეგ ყველაფერი გამოსახეთ console-ში 
let car = {
    company : "BMW",
    model : "M4",
    milage : 45000,
    year: 2018,
    condition: "good",
}



car.color = "black"
car.price = 79700

delete car.milage


console.log(car)