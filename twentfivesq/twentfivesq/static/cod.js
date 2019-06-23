function cod() { 
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
			
	sessionStorage.category = "o"		
		}
	   
	
	   
  else {
	    sessionStorage.homes = "HOME";
		sessionStorage.vises = "VISITOR";
		sessionStorage.category = "";
  }	 
  
}