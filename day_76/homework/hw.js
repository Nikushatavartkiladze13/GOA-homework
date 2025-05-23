function backgroundModerl(){
    let color = document.getElementById('background_moder').value

    if (color){
        document.body.style.backgroundColor = color;
    }
}

let display = document.getElementById('input_2')

function element(Element){
    display.value = display.value + Element
}

function calculate(){
    try{
        display.value = eval(display.value)
    }
    catch(error){
        display.value = 'None'
    }
}

function clean(){
    display.value = ''
}

function Delete(){
    display.value = display.value.slice(0, -1)
}

function procent(){
    display.value = display.value / 100
}