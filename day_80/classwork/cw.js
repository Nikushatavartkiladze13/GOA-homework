// 1) საიტზე დაამატეთ ტექსტი. გაუწერეთ მას Javascript-ის კოდი ისე, რომ ტექსტზე დაჭერისას შეიცვალოს იგი და ეკრანზე მის ნაცვლად გამოვიდეს ახალი წინადადება;


let myH1 = document.getElementById("h1")

myH1.style.cursor = "pointer"

myH1.addEventListener("click", function(){
    myH1.textContent = "GOAl-oriented academy"
})


