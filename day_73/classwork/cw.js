//  შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა სია შემდეგ კი დაბეჭდეთ ამ სიის ჯამი
function myList(arr){
    let num = 0
    for(let i of arr){
        num += i
    }
    console.log(num)
}

myList([1,2,3,4,5,6,7,8,9,10])