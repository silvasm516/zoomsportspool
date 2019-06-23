// Steve Silva 5/18/2016

//function rndo() generates ten random numbers between 0 and 9 inclusive.

function rndo(){
    var horse = [];
	var mule = [];
	var raccoon = [];
	var frog = [];
	var shark = [];
	var raven = [];
	var crow = [];
for(var monkey = 0; monkey < 2; monkey++) {	
/*generate an array of ten random numbers between
1 and 1,000,000, called ran[]. Create object 'place'*/
var place = new Object;
var ran = [];
for (var r=0; r<10; r++){
var item =  Math.floor((Math.random() * 1000000)+ 1);
ran.push(item);
}

/* define the random numbers as properties of place
and assign the property values 1 to 10 to each of the ten 
random numbers(one number value to each property)*/ 

for(var x = 0; x < 10; x++){
var dog = ran[x];
var pup = dog.toString();
var num = x;
var n = num.toString();
place[pup] = n;
}

/*Sort the random nubers in ascending order, then access the 
property values, which have now been randomly mixed. Return the
values as textContent.*/

ran.sort(function(a, b){return a -b});
if (monkey ==0){
for(var z = 0; z < 10; z++){
var prePreAns  = ran[z];
var preAns = prePreAns.toString();
var ans = place[preAns];
horse.push(ans);
}
}
if(monkey ==1){
for(var j = 0; j < 10; j++){
var prePreAnsr  = ran[j];
var preAnsr = prePreAnsr.toString();
var ansr = place[preAnsr];
raccoon.push(ansr)
}
}  
}

    
        crow = horse.join('');
		raven = raccoon.join('');
		var s = 0;
		var t = 0;
		for(var q = 0; q < 10; q++) { 
		
		    mule[q] = document.getElementById("b"+ q+q+q);
			   
		    
			mule[q].textContent = crow[s] // raven[p];
		    s = s + 1;
			
		}
		for(var q = 10; q < 20; q++) { 
		
		    mule[q] = document.getElementById("b"+ q+q+q);
			   
		    
			mule[q].textContent = raven[t] // raven[p];
		    t = t + 1;
			
		}
var justTxt = document.getElementById("sortedNums");
justTxt.textContent = justTxt.textContent + ans
 } 



/*var count = 10000;
var tot = 0;
function randTest (count){
var k = 1;
for(t = 0; t < count; t++){
rndo();
var rat = parseInt(ans);
var j = k % 4;
if(j ==0){
   tot = tot + rat;
   
 }
 k = k + 1;
 }
 return tot;
} 
randTest(count);
var result = (tot/count)*4;


window.alert(tot);
window.alert(count);
window.alert(result);*/


