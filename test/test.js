thing = document.getElementById('typing').innerHTML;
console.log(thing);
listThing = thing.split(" ");
console.log(listThing);
//n is counter for the array of words in the prompt
n = 0;


var toCheck = function() {
    //inputThing gets the text boxes text
    inputThing = document.getElementById('inputText').value;
    //if finished the prompt, alerts the user and sets the index to -1 to prevent infinite loop
    if (n === listThing.length) {
      alert('congratz');
      n = -1;
    }
    //tracks the word the user needs to type, if it equals -1, it shows Finished!
    if (n != -1) {
      document.getElementById('wordUpTo').innerHTML = listThing[n];
    }
    else{
      document.getElementById('wordUpTo').innerHTML = "Finished!";
    }
    //if textbox matches the word, it clears the textbox, raises the word array counter
    if ((listThing[n] + " ") === inputThing){
      document.getElementById('inputText').value = "";
      n++;
      console.log("yay!");
      return true;
    }
};

setInterval(toCheck, 1);
function getTextBox(){
    inputThing = document.getElementById('inputText').value;
    return inputThing;
};

console.log(thing[3]);
