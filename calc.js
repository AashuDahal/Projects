let screen=document.getElementById("display")
let num1;
let num2;
function display(x){
    screen.value+=x;
}
function calculate(){
    num1=screen.value;
    num2=eval(num1);
    screen.value=num2;
}
function empty(){
    screen.value=' ';
}