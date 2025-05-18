// 2) მომხმარებელს შემოატანინეთ რიცხვი, შემდეგ შემოატანინეთ არჩევანი(ერთიდან მომხმარებლის რიცხვამდე დაბეჭდოს ლუწი, კენტი, კვადრატი ან 3 ის ჯერადი რიცხვი


let userNumber = Number(prompt("Enter your number: "))
let userChoice = prompt("enter choice: ")


let i = 1


while(i < userNumber){
    if(i % 2==0  &&  userChoice == "luwi"  ){
        console.log(i)
    }else if(i % 2==1 && userChoice == "kenti"){
        console.log(i)
    }else if(userChoice=="kvadrati"){
        console.log(i ** 2)

    }else if(i % 3 == 0 && userChoice == "samisjeradi"){
        console.log(i)
    }else{
        break
    }

i++ 



}





























