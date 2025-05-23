// 1)შექმენით ობიექტი car , რომელსაც ექნება 5 key -  company(მწარმოებელი) , model , milage ,year , condition , ამ ობიექტში ასევე უნდა იყოს შენახული ფუნქცია , ამ ფუნქციას პარამეტრად ჰქონდეს condition ,და ამ ფუნქციაში შეამოწმეთ , რომ თუ condition-არის კარგი ან ცუდი დაბეჭდეთ შემდეგი ტექსტი car is in {condition} condition გამოიყენეთ format-ი



let car = {
    company : "BMW",
    model : "M4",
    milage : 45.000,
    year: 2018,
    condition: "good",
    carCondition(condition){
        if(condition === "good" || condition === "bad"){
            return `car is in ${condition} condition`
        }
    }

}

// console.log(carCondition(car.condition))
console.log(car.carCondition(car.condition));
