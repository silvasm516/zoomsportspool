function downDate() {
	var k = [1, 4, 13, 18, 22];
	for(var g = 0; g < k.length; g++){
		k[g] = var property;	
		var stat = squares.indexOf(property);
	        if (tracker[stat] == 1) {
	            property.style.backgroundColor = "#9FCBC5";
				property.parentElement.style.backgroundColor = "#9FCBC5"; 
			    tracker[stat] = 0;
				var tar = property;
			//	window.alert(tar);
				holder.splice(holder.indexOf(property), 1);
	        }
	        else {
	            property.style.backgroundColor = "#08088A";
				property.parentElement.style.backgroundColor = "#08088A"; 
	            tracker[stat] = 1;
				var ant = property;
				holder.push(ant);
				var h = h + 1;
				//alert(ant)	
	        }
	 }
}