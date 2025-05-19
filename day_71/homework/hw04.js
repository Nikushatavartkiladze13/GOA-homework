// 5)Splice მეთოდის გამოყენებით ჩაანაცვლეთ სიაში ყველა უარყოფითი რიცხვი 0 - ით


let myArray = [1,2,3,4,5,6,7,8,9,10,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]

for(let i = 0 ; i<myArray.length; i++){
    if(myArray[i] < 0) {
        myArray.splice(i, 1, 0)
    }
}


console.log(myArray)