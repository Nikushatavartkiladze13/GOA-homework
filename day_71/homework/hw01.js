// 2)for-ციკლის გამოყენებით იპოვეთ სიაში ყველაზე დიდი და ყველაზე პატარა რიცხვები


let myArray = [1,2,3,4,5,6,7,8,9,10]

let max = myArray[0]
let min = myArray[0]


for(let i of myArray){
    if(i > max){
        max = i
    }if(i < min){
        min = i 
    }
}

console.log(max, min)