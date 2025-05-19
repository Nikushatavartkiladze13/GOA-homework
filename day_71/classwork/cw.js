//  1) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი დაითვალეთ ერთიდან მომხმარებლსი შემოტანილ რიცხვამდე მხოლოდ ლუწი რიცხვების ჯამი, გამოიყენეთ fo
let userNumber = Number(prompt("enter your number: "))
let num = 0


for(let i = 0; i < userNumber ; i++){
    if(i % 2 == 0){
        num += i
        
    }
   
}
console.log(num)


