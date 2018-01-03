thing = document.getElementById('typing').innerHTML;
console.log(thing);
listThing = thing.split(" ");
console.log(listThing);
function toCheck() {
    inputThing = document.getElementById('inputText').value;
    if (thing === inputThing){
	return true;
	alert("!!!");
    }
};
setInterval(toCheck,1);

function getTextBox(){
    inputThing = document.getElementById('inputText').value;
    return inputThing;
};
