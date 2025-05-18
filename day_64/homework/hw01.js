// შექმენით 4 ცვლადი თითოეულ მათგანს მნიშვნელობად მიანიჭეთ განსხავებული რიცხვები შემდეგ კი ამ რიცხვებით რომლებსაც ინახავთ ცვლადებში ყველა შესაძლო კომბინაციით შეასრულეთ ოთხი მათემატიკური მოქმედება: მიმატება, გამოკლება, გამრავლება, გაყოფა ისე რომ დაიბეჭდოს თვითონ მოქმედება და პასუხი მაგ. ავიღოთ ორი რიცხვი 3 და 4 ამ ორი რიცხვის შემთხვევაში შედექი იქნება 3 + 4 = 7
// 3 - 4 = -1 და ასე შემდეგ ყველა შესაძლო რიცხვების კომბინაციით და მოქმედებით


var num1 = Number(prompt("Enter your Number: "))
var num2 = Number(prompt("Enter your Number: "))
var num3 = Number(prompt("Enter your Number: "))
var num4 = Number(prompt("Enter your Number: "))

console.log(num1, "+", num2, "+", num3, "+", num4, "=", num1 + num2 + num3 + num4)
console.log(num1, "-", num2, "-", num3, "-", num4, "=", num1 - num2 - num3 - num4)
console.log(num1, "/", num2, "/", num3, "/", num4, "=", num1 / num2 / num3 / num4)
console.log(num1, "*", num2, "*", num3, "*", num4, "=", num1 * num2 * num3 * num4)