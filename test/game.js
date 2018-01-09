var prompt = document.getElementById('typing').innerHTML;
console.log(prompt);
var promptNumWords = prompt.split(" ");
//removes elements with nothing in them

while($.inArray("", promptNumWords) != -1){
  promptNumWords.splice($.inArray("", promptNumWords), 1);
}
console.log(promptNumWords.indexOf(""));
console.log(promptNumWords);


//n is counter for the array of words in the prompt
var n = 0;
var start;
//t is used to keep track of when a correct word was typed
var t = 0;
var typedPrompt = '';
var leftPrompt = prompt;


var toCheck = function() {
    //inputThing gets the text boxes text
    inputThing = document.getElementById('inputText').value;
    //if finished the prompt and sets the index to -1 to prevent infinite loop
    if (n === promptNumWords.length) {
	n = -1;
	t = 0;
    }

    if (n >= 0) {
	document.getElementById('wordUpTo').innerHTML = promptNumWords[n];
	var typing = document.getElementById('typing');
	if(t === 1){
	    var typed = document.getElementById('typed');
	    //add the word already typed to typedPrompt
	    typedPrompt += promptNumWords[n-1] + " ";
	    typed.innerHTML = typedPrompt;
	    //remove the typed word from leftPrompt
	    leftPrompt = leftPrompt.replace(promptNumWords[n-1], " ");
	    typing.innerHTML = leftPrompt;
	    t = 0;
	}
	//making the current word red
	typing.innerHTML = leftPrompt.replace(promptNumWords[n], "<div style=\"color: red; display: inline; \">" + promptNumWords[n] + "</div>");
	
    }
    else if(n === -1){
      var elapsed = (new Date().getTime() - start) / 1000;
      var wpm = Math.floor((prompt.length/5) / (elapsed/60));
      document.getElementById('wpm').innerHTML = wpm;
      n = -2;
    }
    else{
        document.getElementById('wordUpTo').innerHTML = "Finished!";
    }
    //if textbox matches the word, it clears the textbox, raises the word array counter
    if ((promptNumWords[n] + " ") === inputThing){
      document.getElementById('inputText').value = "";
	n++;
	t = 1;
      console.log("yay!");
      return true;
    }
};

setInterval(toCheck, 1);
function getTextBox(){
    inputThing = document.getElementById('inputText').value;
    return inputThing;
};

$('#inputText').one("keyup", function(){
   start = new Date().getTime();
});


