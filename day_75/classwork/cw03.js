// 3)Prompით მომხმარებელს შემოატანინეთ მისი სახელი, გვარი, ასაკი და ჰობი, შემდეგ ეს ინფორმაცია შეინახეთ ობიექტში, ასევე ამ ობიექტს დაუმატეთ ფუნქცია, რომლის გამოძახებაზეც კონსოლში გამოიტანს "Welcome {name}"



let userName = {
    firstName : prompt("enter your name: "),
    lastName : prompt("enter your lastname: "),
    welcome(){
        console.log("hello " + this.firstName + " " + this.lastName)
    }
}


userName.welcome()