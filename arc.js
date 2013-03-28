function renderArcGraph(filename) {
	d3.json(filename, function(jsondata) {
		var nodes = jsondata['nodes'];
		var arcs = jsondata['arcs'];
		var width = 1100;
		var height = 768;
		var node_width = width / nodes.length;
		var y = height * 0.8;
		var x = d3.scale.ordinal()
			.domain(d3.range(nodes.length))
			.rangeBands([0, width])

		//sets up the basic container for the visualization
		var chart = d3.select("#arc")
			.append("svg")
			.attr("class", "chart")
			.attr("width", width)
			.attr("height", height)
		
		chart.selectAll("rect")
			.data(nodes)	
			.enter()
			.append("rect")
			.attr("width", node_width)
			.attr("height", 15)
			.attr("x", function(d, i) { return x(i); } )
			.attr("y", y)
			.attr("fill", function(d) { return d.color; })
			.append("title")
			.text(function(d) { return d.name; })

		var arcGroup = chart.append("g")
			.attr("id", "arcspaths");
		console.log(arcs.length);

		//draw the arcs from one frame to the other
		arcGroup.selectAll("path")
			.data(arcs)
			.enter().append("path")
			.attr("d",function(d,i){
			    //x2 is always the rightmost, so 
			    //swap the values if neccessary
				var point_a_x =  x(d[0]);  
				var point_b_x = x(d[1]);
				if(point_a_x > point_b_x){
					x1 = point_b_x;
					x2 = point_a_x;
				}
				else{
					x1 = point_a_x;
					x2 = point_b_x;
				}
				x1 = x1 + node_width/2;
				x2 = x2 + node_width/2;
				//qick calculation for the arc.  The closer the
				//teams are to each other (on the axis), the 
				//smaller the radii need to be
				val = (x2 - x1)/2;
			    return "M" + x1 + ","+y+" A "+ val +","+ val +" 0 0 1 " + x2 + ","+y
			})
			.attr("stroke", function(d) {return nodes[d[0]].color;})
			.attr("stroke-width", node_width)
			.attr("fill","none") 
	})

}

//based on code from: http://mbostock.github.com/d3/ex/chord.html
function fade(opacity, teams) {
	return function(g, i) {
    //fade the paths 
		var paths = d3.select("#trades").selectAll("path").filter(function(d) {
			return d.team_a != teams[i] && d.team_b != teams[i];
		});
		paths.transition().style("opacity", opacity);

    //fade the images
    //these are the trades that go with the selected team
		var items = $.grep(d3.select("#trades").selectAll("path").data(), function(item) {
			return $.inArray(item, paths.data()) < 0;
		});
    //get the team a and team b of the trade
		var involvedTeams = $.map(items, function(value, index) {
			return [value.team_a, value.team_b];
		});
    //grab all the images that aren't in the list
    //of teams built above
		d3.select("#trades").selectAll("image").filter(function(d) {
			return $.inArray(d, involvedTeams) == -1;
		}).transition().style("opacity", opacity);
	};
}