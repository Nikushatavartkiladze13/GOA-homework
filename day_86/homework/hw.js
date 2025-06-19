// 1)შექმენით ცვლადი word - გადაეცით თქვენთვის სასურველი სიტყვა, შემდეგ მომხმარებელს შემოატანინეთ სასუველი ენა(მაგ:ქართული,ინგლისური,ფრანგული) და switch-კონსტრუქტორის გამოყენებით გააკეთეთ მარტივი translate როდესაც მომხმარებელი შემოიყვანს მაგალითად "ფრანგულს" თქვენი სიტყვა კონსოლში გადაითარგმნოს "ფრანგულად", ხოლო თუ მომხმარებელი შემოიტანს სხვა სიტყვას მაგ შემთხვევაში კონსოლში გამოიტანოს რომ ასეთი ენა არ არსებობს და ახლიდან სთხოვოს შეყვენა


let txt = "მსოფლიოში საუკეთესო აკადემია."
let language = prompt("enter your language")

switch(language){
    case "Georgia":
        console.log(txt)
        break
    case "English":
        txt = "The best academy in the world."
        console.log(txt)
        break
    case "French":
        txt = "La meilleure academie du monde."
        console.log(txt)
        break
    default:
        console.log("There is no such language.")
}
