
	
   
    
	var h = 0;
	
	var tracker = [];
	var holder = []; 
	var squares = ["a1","a2","a3","a4","a5","a6","a7","a8","a9","a10","a11","a12","a13","a14","a15","a16","a17","a18","a19","a20","a21","a22","a23","a24","a25"];
	for(var n = 0; n < 26; n++) {
		    tracker[n] = 0;
			}
	 var counterx = 0;
	 var monkey = 0;
	 
	$(document).ready(function(){
	$(".proList1").chosen();
	});
	
	$(".proList1").chosen(); 

	
   // var fox =  document.getElementById("proList1");
	//if (fox.addEventListener){fox.addEventListener("change",alert("kill"), false);
	//			}
	//$(".proList2").chosen();
	
	 
	
	
   // $(document).ready(function(){
	//	$("proList1").chosen().change (function(){
     //   if ("proList1"==="HOMIE") {
		//   formKill()
		//			};
					
	//	})

//	})		
		
    //$(".proList1").chosen();
    //create_option: true, persistent_create_option: true, skip_no_results: true;
    // persistent_create_option decides if you can add any term, even if part
    // of the term is also found, or only unique, not overlapping terms
   
    // with the skip_no_results option you can disable the 'No results match..' 
    // message, which is somewhat redundant when option adding is enabled
   
 

	 
	// $(".proList").chosen()
	// $(".chosen-select").chosen()
//********************************************************************************************************************/
	function setColor() {
	    var property = this;
		var stat = squares.indexOf(property.id);
        if (tracker[stat] == 1) {
            property.style.backgroundColor = "#FFFFFF";
			property.parentElement.style.backgroundColor = "#FFFFFF"; 
		    tracker[stat] = 0;
			var tar = property.textContent;
		//	window.alert(tar);
			holder.splice(holder.indexOf(property.textContent), 1);
        }
        else {
            property.style.backgroundColor = "#08088A";
			property.parentElement.style.backgroundColor = "#08088A"; 
            tracker[stat] = 1;
			var ant = property.innerHTML;
			holder.push(ant);
			var h = h + 1;
		
        }
		
    }
//********************************************************************************************************************//	
	function setName() {
	
			 var colors_list =["#FFFFFF", "#58D3F7", "#FE9A2E", "#F4FA58", "#BDBDBD", "#B18904"];
	         if (counterx == 0) { 
				       localStorage.setItem('counter', counterx);
					   monkey = localStorage.counter % 6;
					   counterx = counterx + 1;
				  }
				  else {
					  localStorage.setItem('counter', counterx);
				      monkey = localStorage.counter % 7;
					  counterx = counterx + 1;
				 }
				
             		 
			 
	         var mole = document.getElementById("home");
			 var counter = 0;
		     for( var c = 0; c < squares.length; c++) {
			     var rat = squares[c];
			     var  item = document.getElementById(rat);
				 //cat[c] = item.innerHTML;
				 for( var t = 0; t < holder.length; t++) { 
				 //var test =  cat.has(holder[t].innerHTML);
				 //alert(test);
				 //test == true ? (counter = counter + 1, cat.add(item.innerHTML)) : "";
				
				  
				 			 
				 item.textContent == holder[t] ?  (item.innerHTML = mole.value , item.style.font ="normal bold 16px arial,serif", item.style.whiteSpace= "normal", item.style.color = colors_list[monkey], item.style.textAlign= "center", item.disabled = true) :  ""; 
				 
				 
				 //alert(test);
				 }
				 //alert(holder[t]);
				} 
				mole.value = ""; 
	           }
//*************************************************************************************************************************//			   
	var count = 1;
	for (var  i = 0; i < 25; i++){
		var squares = ["a1","a2","a3","a4","a5","a6","a7","a8","a9","a10","a11","a12","a13","a14","a15","a16","a17","a18","a19","a20","a21","a22","a23","a24","a25"];
		
		<!-- var containrs = ["a101","a102","a103","a104","a105","a106","a107","a108","a109","a110","a111","a112","a113","a114","a115","a116","a117","a118","a119","a120","a121","a122","a123","a124","a125","b1000"]
 
		var dog =  document.getElementById(squares[i]);
	   
		
		if(dog.addEventListener) {dog.addEventListener("click",setColor, false);
			} 
			 else if(dog.attachEvent) {
			 dog.attachEvent("onclick", setColor);
			 }  
         }
	
	
	
	var pig =  document.getElementById("submit");
        
	if(pig.addEventListener) {pig.addEventListener("click",setName, false);
			} 
			 else if(pig.attachEvent) {
			 pig.attachEvent("onclick", setName); 
			 }
	
	
	
   /* var cow =  document.getElementById("teams");
        
	if(cow.addEventListener) {cow.addEventListener("click",enterTeams, false);
			} 
			 else if(cow.attachEvent) {
			 cow.attachEvent("onclick", enterTeams); 
			 }	

			 
			 
    var steer =  document.getElementById("colteams");
        
	if(steer.addEventListener) {steer.addEventListener("click",makeTeams, false);
			} 
			 else if(steer.attachEvent) {
			 steer.attachEvent("onclick", makeTeams); 
			 }		*/		 
			 
			 

//******************************************************************************************************************************///	
function enterTeams(A, B) {
	var alpha = A
	if (alpha.value == 17) {
	var customHt = document.createElement("select");
	customHt.setAttribute("width","250"); 
	alpha.appendChild(customHt);
	
	}
	else {
			var team = document.getElementsByClassName('pro');
			var beta = alpha;
			var eggH = document.createElement("img");
			eggH.setAttribute("src", "pool/thumbsPro/" + beta + ".png");
			eggH.setAttribute("height" , "40");
			eggH.setAttribute ("width" , "50");
			eggH.setAttribute("padding", "0");
			var lambH = document.getElementById("teamLog");
			lambH.appendChild(eggH);
	}
    <!-- var team2 = document.getElementsByClassName('pro'); -->
	<!-- var delta = document.getElementById("proList2"); -->
	var pi = B
	var eggH2 = document.createElement("img");
    eggH2.setAttribute("src", "pool/thumbsPro/" + pi + ".png");
    eggH2.setAttribute("height" , "40");
	eggH2.setAttribute ("width" , "50");
	eggH2.setAttribute("padding", "0");
	var lambH2 = document.getElementById("teamLog2");
	lambH2.appendChild(eggH2);
	
	
	var calfH = beta.textContent;
	var gamma = document.getElementById("hTeam");
	gamma.style.textAlign = "center";
    //var calfV = document.getElementById("teamV").value;
    document.getElementById("hTeam").textContent = beta;
	document.getElementById("hTeam").style.font="normal bold 32px arial,serif";
	document.getElementById("vTeam").textContent = pi;
	document.getElementById("vTeam").style.font="normal bold 32px arial,serif"; 
	}
//********************************************************************************************************************************///
function makeTeams(A, B) {
	
     <!-- var team = document.getElementsByClassName('col');  -->
	 <!-- var alpha = document.getElementById("colSel");  -->
	 
	var team = document.getElementsByClassName('col'); 
	var alpha = A
	
	var beta = "Homie"
	var ext = ".jpg"
	<!-- var cappa = alpha -->
	var cappa = beta;
	for (var a = 0; a < team.length / 2; a ++) { 
		if (alpha == team[a].value){
			var sigma = team[a].label;
		    beta = team[sigma].value
			cappa = beta;
			var ext = ".png"
		}	
		
	}
			
	var eggH = document.createElement("img");
    eggH.setAttribute("src", "pool/thumbs/" + cappa + ext);
    eggH.setAttribute("height" , "40");
	eggH.setAttribute ("width" , "50");
	eggH.setAttribute("padding", "0");
	var lambH = document.getElementById("teamLog");
	lambH.appendChild(eggH);
	
	
    var team = document.getElementsByClassName('col');
	var alpha2 = B
	
	var beta2 = "Visor"
	var ext2 = ".jpg"
	var cappa2 = beta2
	
	for (var z = 0; z < team.length; z ++) { 
		if (alpha2 == team[z].value){
			var sigma2 = team[z].label;
			var beta2 = team[sigma2].value
			cappa2 = beta2;
			ext2 = ".png"
		}
			
	}
	
	var eggH2 = document.createElement("img");
    eggH2.setAttribute("src", "pool/thumbs/" + cappa2 + ext2);
    eggH2.setAttribute("height" , "40");
	eggH2.setAttribute ("width" , "50");
	eggH2.setAttribute("padding", "0");
	var lambH2 = document.getElementById("teamLog2");
	lambH2.appendChild(eggH2);
	
	
	
	//var calfH = team[beta].textContent;
	var calfH = beta;
	var gamma = document.getElementById("hTeam");
	gamma.style.textAlign = "center";
    //var calfV = document.getElementById("teamV").value;
	
	<!-- document.getElementById("hTeam").textContent = cappa; -->
    document.getElementById("hTeam").textContent = alpha;
	document.getElementById("hTeam").style.font="normal bold 32px arial,serif";
	<!-- document.getElementById("vTeam").textContent = cappa2; -->
	document.getElementById("vTeam").textContent = alpha2;
	document.getElementById("vTeam").style.font="normal bold 32px arial,serif";
	
	}




//***********************************************************************************************************************************//	
<!-- function rndSortt(){
	<!-- var horse = [];
//	var mule = [];
//	var raccoon = [];
//	var frog = [];
//	var shark = [];
//	var raven = [];
//	var crow = []; -->
	
/*	var space = document.getElementById("arraay");
	var ship = document.getElementById("morarray");
	/*for(var z = 0; z <10; z++) {
	<!-- var g =  Math.floor((Math.random() * 10) + 1); -->
	    horse.push(Math.floor((Math.random() * 999) + 1));
	    mule.push(horse[z]);
		window.alert(horse[z]);    		
	 }
	horse.sort();
	}*/
/*	var limit = 10;
    var amount = 10;
    var lower_bound = 0;
    var upper_bound = 9;    

if (amount > limit){ limit = amount; //Infinite loop if you want more unique
                            }        //Natural numbers than existemt in a
for (var e =0; e < 2; e++){
if (e == 0) {                                  // given range
	while (horse.length < limit) {
		var fish = Math.round(Math.random()*(upper_bound - lower_bound) + lower_bound);
		if (horse.indexOf(fish) == -1) { 
			// Yay! new random number
			horse.push( fish );
		}
	}
}
                                 
else if (e == 1){
    while (raccoon.length < limit) {
		var crab = Math.round(Math.random()*(upper_bound - lower_bound) + lower_bound);
		if (raccoon.indexOf(crab) == -1) { 
			// Yay! new random number
		   raccoon.push( crab );
		}
	
	}
	
}
 
} 	
	/*	var t = mule[p];
		var l = 0;
		var r = 9;
		var  m =  Math.floor(((l+r))/2);
		for (var p = 0; p <10; p++) { 
		  while (t != horse[m]){
			   
			   if(l > r) {  m = Math.floor(((l+r))/2);
			   } else if (horse[m] < t) { (l = m + 1);   
			   }  else if (horse[m] > t ){ ( r = m - 1); 
					
				} else if (t== horse[m]) {raccoon[p] = t; ;
					
					m =  Math.floor(((l+r))/2);
						
				} 
		  
		 }
		window.alert(m);  */
 -->	  
	<!--  horse.sort(function() { return 0.5 - Math.random()}); --> -->
	  

	/*for(var o = 0; o <10; o++) {
	  var monkey = (raccoon[o]); 
		//var rat = horse.indexOf(monkey);*/
		
		
		<!-- shark = horse.toString();
		//frog = raccoon.toString(); -->
	/*	crow = horse.join('');
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
	   /* space.textContent = space.textContent +  lion;
		ship.textContent = ship.textContent + tiger;*/
	<!-- } --> -->
//***************************************************************************************************************************************///
	<!-- function prnt() 
	     

    
    

		
	<!-- /*	var zoomWindow = window.open("", "zoomwin","width=1060,height=800");
		/*var zoomWindow = window.open("","SpecsWindow","toolbar=no,menubar=no,location=no,scrollbars=no,resizable=no,width=380,height=405");
		zoomWindow.focus();*/
		/*document.write("<canvas id='example' width='200' height='200'></canvas>");
		
		var example = document.getElementById('example');
		var context = example.getContext('2d');
		context.fillStyle = 'red';
		context.fillRect(30, 30, 50, 50);
		window.open("Grid 4.html")
	 }  */ --> -->
//*******************************************************************************************************************************************/// 
	 
	<!-- r = document.getElementById("rand");
	
	<!-- if(r.addEventListener) {r.addEventListener("click",rndSortt, false);
			<!-- }  -->
			<!--  else if(r.attachEvent) {
			<!-- r.attachEvent("onclick", rndSortt); 
			<!--  } --> --> --> -->
   <!--  pr = document.getElementById("prnt"); -->
	
	<!-- if(pr.addEventListener) {pr.addEventListener("click", prnt, false);
			<!-- } 
			 <!-- else if(pr.attachEvent) { -->
			<!-- pr.attachEvent("onclick", prnt); 
			<!-- } --> -- -->> -->
			 -->
	 
			 
			 




			
var fat = document.getElementById("fog");
  if (fat.addEventListener) {
  fat.addEventListener("click", rndo,
  false); 
  } else if (fat.attachEvent) {
  fat.attachEvent("onclick", rndo);
  }
 
function go(X, Y, Z) {
  X = sessionStorage.homes;
  Y = sessionStorage.vises;
  Z = sessionStorage.category
  
  if (Z == "p") { 
		enterTeams(X, Y);
}
  else  if ( Z == "c") {
		makeTeams(X, Y)
}
  else {
		makeTeams(X, Y)
}
}
		
go( sessionStorage.homes, sessionStorage.vises, sessionStorage.category)