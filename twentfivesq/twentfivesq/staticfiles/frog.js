function frog() {
	t = document.getElementById("homeTeam");
	u = document.getElementById("visitingTeam");
	ee = document.getElementsByClassName("panel-body");
	for(z = 1; z < 11; z ++){
		if(ee[z].textContent == "home visitor"){
			ee[z].textContent = t + " " + u 
			return
		}