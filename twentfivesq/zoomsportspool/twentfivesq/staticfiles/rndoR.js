// Steve Silva 5/18/2016

//function rndo() generates ten random numbers between 0 and 9 inclusive.

function rndo(){
	var pr = "10px";
	var pl = "10px";
    var A = "#BDBDBD";
	var B = "#000000"
	var C = "#DF3A01";
    var horse = [];
	var mule = [];
	var raccoon = [];
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
and assign the property values 0 to 9 to each of the ten 
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
			if (q  == 3  || q  == 4 || q  == 7  || q  == 8)  {
				mule[q].style.color =  C;
				mule[q].style.paddingLeft = pl;
				mule[q].style.paddingRight = pr
			}
			else
			{
				mule[q].style.paddingLeft = pl;
				mule[q].style.paddingRight = pr
				mule[q].style.color =  B;
			}
			mule[q].style.paddingLeft = pl;
			mule[q].style.paddingRight = pr
			mule[q].style.background = A;
		    s = s + 1;
			
		}
		for(var q = 10; q < 20; q++) { 
		
		    mule[q] = document.getElementById("b"+ q+q+q);
			   
		    
			mule[q].textContent = raven[t] // raven[p];
			if (q == 11 || q  == 13  || q  == 16 || q  == 18) {
				mule[q].style.color = B;
				mule[q].style.paddingLeft = pl;
				mule[q].style.paddingRight = pr
		}		
		else
			{
				mule[q].style.color =  C;
				mule[q].style.paddingLeft = pl;
				mule[q].style.paddingRight = pr
			}
		mule[q].style.paddingLeft = pl;
		mule[q].style.paddingRight = pr;
		mule[q].style.background = A;		
		t = t + 1;
			
		}
var justTxt = document.getElementById("sortedNums");
justTxt.textContent = justTxt.textContent + ans
 } 