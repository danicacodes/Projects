// Declare Variables
// Added IDs in index.html file
//var datetime = d3.select('#date');
//var city = d3.select('#city');
//var state = d3.select('#statefilter');
//var country = d3.select('#country');
//var shape = d3.select('#shapefilter');
//var duration = d3.select('#duration');
//var comments = d3.select('#comments');

// Use let instead of var to declare a variable in code to show error code 'undefined'    
//var button = d3.select('#filter-btn');
let button = d3.select('#filter-btn');

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
    // Use let instead of var to declare a variable in code to show error code 'undefined'
    let newdate = d3.select('#datetime').property("value");
    let newState = d3.select('#statefilter').property("value");
    let newShape = d3.select('#shapefilter').property("value");
    
    if (newdate !=''){
        console.log("Button Clicked for Date!");
        tbody.html("");

        let newdate = d3.select('#datetime').property("value");
        console.log(newdate);

        let outputData = data.filter(function(filterData) {
        return(filterData.datetime === newdate);
    });
    
        console.log(outputData);
        outputData.forEach((ufo_sightings) => {
            console.log(ufo_sightings);
            let row = tbody.append('tr'); //appending tr tag that doesn't exist so it is creating one
            Object.entries(ufo_sightings).forEach(([key, value]) => {
                console.log(key, value);
                let cell = row.append('td');
                cell.text(value);
    
            });
        });
    };

    if (newState !=''){
        console.log("Button Clicked for State!");
        // tbody.html('');

        let newState = d3.select('#statefilter').property("value");
        console.log(newState);
        
        let outputData = data.filter(function(filterData) {
            console.log(filterData);
            return(filterData.state === newState);
        
        });

        console.log(outputData); // This is returning an empty array
        outputData.forEach((ufo_sightings) => {
            console.log(ufo_sightings);
            let row = tbody.append('tr'); //appending tr tag that doesn't exist so it is creating one
            Object.entries(ufo_sightings).forEach(([key, value]) => {
                console.log(key, value);
                let cell = row.append('td');
                cell.text(value);
    
            });
        });

    };

    if (newShape !=''){
        console.log('Button Clicked for Shape!');
        // tbody.html('');

        let newShape = d3.select('#shapefilter').property('value');
        console.log(newShape);

        let outputData = data.filter(function(filterData) {
        return(filterData.shape == newShape);
        });

        console.log(outputData);
        outputData.forEach((ufo_sightings) => {
            console.log(ufo_sightings);
            let row = tbody.append('tr'); //appending tr tag that doesn't exist so it is creating one
            Object.entries(ufo_sightings).forEach(([key, value]) => {
                console.log(key, value);
                let cell = row.append('td');
                cell.text(value);
    
            });
        });
    };
    
});// Closes button click

