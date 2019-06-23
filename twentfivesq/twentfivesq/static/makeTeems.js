function makeTeems(A, B) {
	
     <!-- var team = document.getElementsByClassName('col');  -->
	 <!-- var alpha = document.getElementById("colSel");  -->
	alert(A)
	alert(B) 
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
var C = cappa;
var E1 = ext
var D = cappa2;
var E2 = ext2

dealTeams(C,E1,D,E2);

}
	



	function go1(X, Y, Z) {
  X = sessionStorage.homes;
  Y = sessionStorage.vises;
  Z = sessionStorage.category
  alert("go one")
 /* if (Z == "p") { 
		enterTeams(X, Y);*/
}
  else  if ( Z == "c") {
		makeTeems(X, Y)
}
  else {
		makeTeems(X, Y)

}
