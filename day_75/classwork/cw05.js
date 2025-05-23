// შექმენით ქვემოთ მოცემული ობიექტის მსგავსი ობიექტი თქვენს სასურველ მანქანაზე და დაამატეთ ფუნქცია CarFullInfo, რომლის გამოძაღებაზეც გამოიტანს მთლიან ინფორმაციას მანქანაზე(აუცილებლად გამოიყენეთ string formatting)



let porsche = {
    carModel: "Porsche 911",
    yearOf: 1964,
    assembly: "Germany",
    designer: "Ferdinad Butz Porsche",
    allInfo(){
        for(let i in porsche){
            return i + " is " + porsche[i]
        }
    }   
}


console.log(porsche.allInfo())