// 4)შექმენი ობიექტი სახელად student რომელსაც ექნება fullName , scores(scores-უნდა იყოს სია რადგან შეინახოთ რამდენიმე მნიშვნელობა) , ასევე ექნება ორი ფუნქცია 1)averageScore()- რომელიც გამოითცლის საშუალო ქულას , 2)checkStudent() - რომელიც გამოითლის მოსწავლის დონეს ქულების მიხედვით , თუ საშუალო ქულა იქნება 90-ზე მეტი გამოსახეთ კონსოლში შემდეგი ტექსტი ("საუკეთესო სტუდენტი")  , თუ საშუალო ქულა იქნება 90 ზე დაბალი და 60 ზე მაღალი გამოსახეთ "კარგი მოსწავლე" , ხოლო თუ საშუალო ქულა იქნება 60 ზე დაბალი გამოსახეთ "ნორმალური მოსწალე"


let student = {
    fullName : "ნიკა თავართქილაძე",
    scores : [90, 70, 90, 60, 85, 83, 78],
    averageScore(){
        let sum = 0 
        for (let i of this.scores){
            sum += i 
        }
        num = sum / this.scores.length 
        return num 
    },
    checkStudent(){
        let avg = num
        if (avg > 90){
            return "საუკეთესო სტუდენტი"

        }else if (avg > 60){
            return "კარგი მოსწავლე"
        }else{
            return "ნორმალური მოსწავლე"
        }
    }
}


console.log(student.averageScore())
console.log(student.checkStudent())
