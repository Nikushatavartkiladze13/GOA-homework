// 4)შექმენით სია სადაც იქნება user-ების სახელი და გვარი და ახალ სიაში დაამატეთ ამ იუსერების  ინიციალები სახელის და გვარის პირველი ასოები, მაგალითად: გიორგი ბიბილაშვილი -> გ.ბ


let myArray = ["ნიკა თავართქილაძე", "გიორგი თავართქილაძე", "საბა თავართქილაძე"]
let emptyList = []
for (let fullName of myArray){
    let parts = fullName.split(" ")
    emptyList.push(parts[0][0] + '.' + parts[1][0])

}

console.log(emptyList)