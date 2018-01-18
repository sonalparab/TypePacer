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
//l is used to keep track if a list was made of the letters in the current word
var l = 0;
var list = [];


var toCheck = function() {
    //inputThing gets the text boxes text
    inputThing = document.getElementById('inputText').value;
    //if finished the prompt and sets the index to -1 to prevent infinite loop
    if (n === promptNumWords.length) {
	n = -1;
	t = 0;
	l = 0;
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
	typing.innerHTML = leftPrompt.replace(promptNumWords[n], "<div style=\"color: hotpink; display: inline; \">" + promptNumWords[n] + "</div>");
	
    }
    //if the prompt was successfully typed, calculate the words per minute
    else if(n === -1){
      var elapsed = (new Date().getTime() - start) / 1000;
      var wpm = Math.floor((prompt.length/5) / (elapsed/60));
      document.getElementById('wpm').innerHTML = wpm;
      n = -2;
      //UPDATE LEADERBOARD
      $.ajax({
        type: "POST",
        url: '/update',
        data: jQuery.param({ newWPM: wpm, 
            current : "" + document.getElementById('user').innerHTML}) ,
            success: function(data){
                console.log("success");
            },
            error: function(data){
                console.log("oof doesnt work");
            }
    });
    }
    else{
        document.getElementById('wordUpTo').innerHTML = 'Finished! If you want to play again click the refresh button';
    }

    //make a list of all the characters in the current word
    // use l to make the list only when the current word changes
    if(l === 0){
	var word = promptNumWords[n];
	var i = 0;
	list = [];
	for(i = 0; i < word.length; i++){
	    list.push(word.charAt(i));
	}
	//update l because the list was made
	l = 1;
    }	
    
    //if textbox matches the word, clear the textbox, raise the word array counter
   if ((promptNumWords[n] + " ") === inputThing){
        document.getElementById('inputText').value = "";
	n++;
	t = 1;
	l = 0;
      console.log("yay!");
      return true;
    }
    //if the textbox does not match the word, check if the current progress is correct
    else{
	var j = 0;
	var correct = true;
	//check if the characters inputed so far match the corresponding
	// characters in the current word
	for(j = 0; j < inputThing.length; j++){
	    if(inputThing.charAt(j) != list[j]){
		correct = false;
	    }
	}
	
	var textbox = document.getElementById('inputText');
	//if an incorrect character was typed, make the textbox red
	if(!correct){
	    textbox.style.backgroundColor = "red";
	}
	//if the characters so far are correct, make the textbox white
	else{
	    textbox.style.backgroundColor = "white";
	}
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


