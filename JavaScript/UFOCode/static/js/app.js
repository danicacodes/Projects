// Declare Variables
// Need to add ids to Index
// this is under a form
var datetime = d3.select('#date');
var city = d3.select('#city');
var state = d3.select('#state');
var country = d3.select('#country');
var shape = d3.select('#shape');
var duration = d3.select('#duration');
var comments = d3.select('#comments');
var button = d3.select('#filter-btn');

// from data.js
var tableData = data;
var tbody = d3.select("tbody"); //tbody tag

function init(){ 
    data.forEach((ufo_sightings) => {
        console.log(ufo_sightings);
        var row = tbody.append('tr'); //appending tr tag that doesn't exist so it is creating one
        Object.entries(ufo_sightings).forEach(([key, value]) => {
            console.log(key, value);
            var cell = row.append('td');
            cell.text(value);
        });
    });
}

init();

// YOUR CODE HERE!
button.on("click", function() {
    console.log("Button Clicked!");
    tbody.html("");

    var newdate = d3.select('#datetime').property("value");
    console.log(newdate);

    var outputData = data.filter(function(filterData) {
        return(filterData.datetime == newdate)
    });
    
        console.log(outputData);
        outputData.forEach((ufo_sightings) => {
            console.log(ufo_sightings);
            var row = tbody.append('tr'); //appending tr tag that doesn't exist so it is creating one
            Object.entries(ufo_sightings).forEach(([key, value]) => {
                console.log(key, value);
                var cell = row.append('td');
                cell.text(value);
    
            });
        });
    });
