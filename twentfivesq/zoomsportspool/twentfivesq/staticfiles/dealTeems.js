function dealTeems (C, D, E1, E2) {

	var eggH = document.createElement("img");
    eggH.setAttribute("src", "../static/thumbs/" + C + E1);
    eggH.setAttribute("height" , "40");
	eggH.setAttribute ("width" , "50");
	eggH.setAttribute("padding", "0");
	var lambH = document.getElementById("teamLog");
	lambH.appendChild(eggH);
	
	
    var eggH2 = document.createElement("img");
    eggH2.setAttribute("src", "../static/thumbs/" + D + E2);
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
	
	<!-- document.getElementById("hTeam").textContent = C; -->
    document.getElementById("hTeam").textContent = alpha;
	document.getElementById("hTeam").style.font="normal bold 32px arial,serif";
	<!-- document.getElementById("vTeam").textContent = D; -->
	document.getElementById("vTeam").textContent = alpha2;
	document.getElementById("vTeam").style.font="normal bold 32px arial,serif";

	}