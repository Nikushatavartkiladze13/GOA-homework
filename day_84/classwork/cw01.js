// 2)შექმენით 4 div-კონტეინერი,თითოეულ დივს მიეცით id , თუ რა ფერი უნდა გახდეს ეს დივი დაკლიკების შემდეგ,ასევე ამ დივში უნდა იყოს პარაგრაფი(Click to see color), შემდეგ javaascript-იდან შეამოწმეთ რომელ DIV-ზე განხორციელდა მოვლენა , ასევე შეამოწმეთ ამ DIV- ის ID-ები და მიანიჭეთ შესაბამისი ფერი ,  ასევე შეცვალეთ paragraph-ის textContent იმ ფერის სახელით რა ფერითაც შეიცვლება დივი


document.addEventListener("click", function(event){
    if(event.target.id == "black"){
        event.target.style.backgroundColor = "black" 
        event.target.style.color = "white" 

    }else if(event.target.id == "blue"){
        event.target.style.backgroundColor = "blue" 
        event.target.style.color = "white" 

    }else if(event.target.id == "red"){
        event.target.style.backgroundColor = "red" 
        event.target.style.color = "white" 

    }else if(event.target.id == "yellow"){
        event.target.style.backgroundColor = "yellow" 
        event.target.style.color = "black" 

    }
})