$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip;   
});

window.addEventListener("load", textParagraphs.bind(null, One, Two, Three, Four), false);


function textParagraphs(One, Two, Three, Four) {
	document.getElementById("t63b").innerHTML = One;
	document.getElementById("t67c").innerHTML = Two; 
	document.getElementById("t75").innerHTML = Three;
	document.getElementById("t78").innerHTML = Four;
}



function Dog() {
	var d = document.getElementById("tit")
	if (d == null) {
		var s = document.getElementById("dash");
		var w = document.getElementById("zoom")

			s.innerHTML = "DASHBOARD"
		}
		/*if(s.innerHTML == "DASHBOARD") {
			w.innerHTML = "";
		}*/
	}	



window.onload = Dog();
window.onload = textParagraphs();


window.addEventListener("load", textParagraphs.bind(null, instrOne, instrTwo, instrThree, instrFour), false);


function textParagraphs(One, Two, Three, Four) {
	document.getElementById("t63b").innerHTML = One;
	document.getElementById("t67c").innerHTML = Two; 
	document.getElementById("t75").innerHTML = Three;
	document.getElementById("t78").innerHTML = Four;
}
    var tad = document.getElementById("ZO");
	var o1 = document.getElementById("Z1");
	var o2 = document.getElementById("Z2");
	var o3 = document.getElementById("Z3");
	var o4 = document.getElementById("Z4");
	var o5 = document.getElementById("Z5");
	var o6 = document.getElementById("Z6");
	var o7 = document.getElementById("Z7");
	var o8 = document.getElementById("Z8");
	var o9 = document.getElementById("Z9");
	

	if(tad.addEventListener) {tad.addEventListener("click", hedge, false);
			 }  
			 else if(tad.attachEvent) { 
			  tad.attachEvent("onclick", hedge);  
			 } 

	if(o1.addEventListener) {o1.addEventListener("click", hedge, false);
			 }  
			 else if(o1.attachEvent) { 
			  o1.attachEvent("onclick", hedge);  
			 } 

	if(o2.addEventListener) {o2.addEventListener("click", hedge, false);
			 }  
			 else if(o2.attachEvent) { 
			  o2.attachEvent("onclick", hedge);  
			 } 		 
	if(o3.addEventListener) {o3.addEventListener("click", hedge, false);
			 }  
			 else if(o2.attachEvent) { 
			  o2.attachEvent("onclick", hedge);  
			 } 		 		 
	if(o4.addEventListener) {o4.addEventListener("click", hedge, false);
			 }  
			 else if(o2.attachEvent) { 
			  o2.attachEvent("onclick", hedge);  
			 } 		 		 

	if(o5.addEventListener) {o5.addEventListener("click", hedge, false);
			 }  
			 else if(o2.attachEvent) { 
			  o2.attachEvent("onclick", hedge);  
			 } 		 		 

	if(o6.addEventListener) {o6.addEventListener("click", hedge, false);
			 }  
			 else if(o2.attachEvent) { 
			  o2.attachEvent("onclick", hedge);  
			 } 		 		 

	if(o7.addEventListener) {o7.addEventListener("click", hedge, false);
			 }  
			 else if(o2.attachEvent) { 
			  o2.attachEvent("onclick", hedge);  
			 } 		 		 


	if(o8.addEventListener) {o8.addEventListener("click", hedge, false);
			 }  
			 else if(o2.attachEvent) { 
			  o2.attachEvent("onclick", hedge);  
			 } 		 		 



	if(o9.addEventListener) {o9.addEventListener("click", hedge, false);
			 }  
			 else if(o2.attachEvent) { 
			  o2.attachEvent("onclick", hedge);  
			 } 		 		 


	// var franken = document.getElementById("stein")

	/*if(franken.addEventListener) {franken.addEventListener("click", hammer,  false);
			 }  
			 else if(franken.attachEvent) { 
			  franken.attachEvent("onclick", hammer);  
			 } */





	var steer =  document.getElementById("subteams510e");


	

        
	if(steer.addEventListener) {steer.addEventListener("click", ling,  false);
			 }  
			 else if(steer.attachEvent) { 
			  steer.attachEvent("onclick", ling );  
			 } 
			 




	if(steer.addEventListener) {steer.addEventListener("click", showAlert, false);
			 }  
			 else if(steer.attachEvent) { 
			  steer.attachEvent("onclick", showAlert );  
			 }
			 
/*	if(steer.addEventListener) {steer.addEventListener("click", bull,  false);
		 }  
			 else if(steer.attachEvent) { 
			  steer.attachEvent("onclick", bull);  
			 } */

	// var beetle =  document.getElementById("sgbutt");



	/*if(beetle.addEventListener) {
		beetle.addEventListener("click", frog,  false);
		}  
		else if(beetle.attachEvent) { 
			beetle.attachEvent("onclick", frog);  
				 } */

//FROM DASHBOARD TO GRID. SETS VALUES FOR GO 
//FUNCTION BY SORTING TEAM LISTS BETWEEN
//PRO, COLLEGE, HOME, VISITOR, AND GAME TYPE	
//VALUES TO SESSION STORAGE VARIABLES. 




			
function ling() { 
	window.alert("ling")
  sessionStorage.homes = "HOME";
  sessionStorage.vises = "VISITOR";
  sessionStorage.category = "";
  var a = document.getElementById("proList1");
  var a1 = a.value;
  var b = document.getElementById("proList2");
  var b1 = b.value;
  var c = document.getElementById("colSel1");
  var c1 = c.value;
  var d = document.getElementById("colSel2");
  var d1 = d.value;
  var e = document.getElementById("otherList1");
  var e1 = e.value;
  var f = document.getElementById("otherList2");
  var f1 = f.value;
 // window.alert(a1.value);
  if( a1 !=  0 ) {
	  sessionStorage.homes = a1; 
	  sessionStorage.vises = b1; 
	  sessionStorage.category = "p"
  }
  else if ( c1 != 0 ) {
      sessionStorage.homes = c1; 
	  
	  if ( d1 != 0 ) { 
			sessionStorage.vises = d1;
		}
	  else {
			sessionStorage.vises = f1;
			}
		sessionStorage.category = "c"	
	  }
  
  
  else if ( e1 != 0)  {
	   sessionStorage.homes = e1; 
	   
	   if ( f1 != 0) { 
	   sessionStorage.vises = f1;
	   }
	   else { 
			sessionStorage.vises = d1;
			}
			
	sessionStorage.category = "c"		
		}
	   
	
	   
  else {
	    sessionStorage.homes = "HOME";
		sessionStorage.vises = "VISITOR";
		sessionStorage.category = "";
  }

 document.getElementById("homeTeam").defaultValue =  sessionStorage.homes 
 document.getElementById("visitingTeam").defaultValue =  sessionStorage.vises 
 cell = document.getElementById("gType") 
 cell.value = sessionStorage.category
 

}






var C = cappa;
var E1 = ext
var D = cappa2;
var E2 = ext2




/* function showAlert(){
  $("#myAlert").addClass("in")
  .delay(3000)
  .fadeOut(function() {
   $(this).remove(); 
});

}*/





function bull()   {
//DEPRECATED
var x = document.getElementById("proList1");
var y = document.getElementById("colSel1");
var z = document.getElementById("otherList1");
var x1 = x.value
var y1 = y.value
var z1 = z.value
if( x1 != 0 ){ var h = x1;}
else if( y1 != 0) { var h = y1;}
else { var h = z1;}

var r = document.getElementById("proList2");
var s = document.getElementById("colSel2");
var t = document.getElementById("otherList2");
var r1 = r.value;
var s1 = s.value;
var t1 = t.value; 
if( r1 != 0) { var v = r1;}
else if( s1 != 0) { var v = s1;}
else { var v = t1;}

var teamP = document.getElementsByClassName("pro");
var teamC = document.getElementsByClassName("col");

for (var p = 0; p < teamP.length / 2; p ++) { 
	if (teamP[p].value == h) {
	h = teamP[p].textContent;
	}
}
for (var c = 0; c < teamC.length / 2; c ++) { 
	if (teamC[c].value == h) {
	h = teamC[c].textContent;
	}	
}	
for (var p = 0; p < teamP.length / 2; p ++) { 
	if (teamP[p].value == v) {
	v = teamP[p].textContent;
	}	
}
for (var c = 0; c < teamC.length / 2; c ++) { 
	if (teamC[c].value == v) {
	v = teamC[c].textContent;
	}	
}
	
var ht = document.getElementById("homeTeam");
var vt = document.getElementById("visitingTeam");

ht.defaultValue = h;
vt.defaultValue = v;

}

function hedge() {
	window.alert("burn");
	var pig = event.srcElement.name
	window.alert(pig.value)
	var hog = document.getElementById("zerot")
	hog.value = pig
	document.getElementById('mongo').click();  
	document.getElementById('stein').click()
	var h = document.getElementById("homT").text.Content;
	 var v = document.getElementById("visT").textContent;
	 var t = document.getElementById("gType").textContent


	 alert(h)
	 alert(v)
	 alert(t)
	 
     sessionStorage.hat = h.value; 
     sessionStorage.vat =  v.value;
     sessionStorage.tap = t.value;
     // window.location.assign('GridEx.html')*/
	 }

</script>