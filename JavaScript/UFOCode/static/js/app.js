// Declare Variables
// Need to add ids to Index
// this is under a form
var datetime = d3.select('#date');
//var city = d3.select('#city');
var state = d3.select('#statefilter');
//var country = d3.select('#country');
var shape = d3.select('#shapefilter');
//var duration = d3.select('#duration');
//var comments = d3.select('#comments');
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
};

init();

//-------------------------------------------------------------------------------------------------//
// YOUR CODE HERE!
button.on("click", function() {
    //console.log("Button Clicked!");
    d3.event.preventDefault();
    tbody.html("");

    //Date Filter
    var newdate = d3.select('#datetime').property("value");
    var newState = d3.select('#statefilter').property("value");
    var newShape = d3.select('#shapefilter').property("value");
    
    if (newdate !=''){
        console.log("Button Clicked for Date!");
        tbody.html("");

        var newdate = d3.select('#datetime').property("value");
        console.log(newdate);

        var outputData = data.filter(function(filterData) {
        return(filterData.datetime === newdate);
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
    };

    if (newState !=''){
        console.log("Button Clicked for State!");
        tbody.html('');

        var newState = d3.select('#statefilter').property("value");
        console.log(newState);

        var outputData = data.filter(function(filterData) {
        return(filterData.statefilter == newState);
        });

        console.log(outputDataState);
        outputData.forEach((ufo_sightings) => {
            console.log(ufo_sightings);
            var row = tbody.append('tr'); //appending tr tag that doesn't exist so it is creating one
            Object.entries(ufo_sightings).forEach(([key, value]) => {
                console.log(key, value);
                var cell = row.append('td');
                cell.text(value);
    
            });
        });

    };

    if (newShape !=''){
        console.log('Button Clicked for Shape!');
        tbody.html('');

        var newShape = d3.select('#shapefilter').property('value');
        console.log(newShape);

        var outputData = data.filter(function(filterData) {
        return(filterData.shapefilter == newShape);
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
    };
    
});// Closes button click

