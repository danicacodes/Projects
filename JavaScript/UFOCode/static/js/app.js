// from data.js
var tableData = data;
var tbody = d3.select("tbody"); //tbody tag

data.forEach((ufo_sightings) => {
    //console.log(ufo_sightings);
    var row = tbody.append('tr'); //appending tr tag that doesn't exist so it is creating one
    Object.entries(ufo_sightings).forEach(([key, value]) => {
        //console.log(key, value);
        var cell = row.append('td');
        cell.text(value);
    });
});

//console.log(data);


// var columns = ['datetime', 'city', 'state', 'country', 'shape', 'durationMinutes', 'comments']

// // ufo_sightings scope is within this function
// data.forEach(function(ufo_sightings){
//     console.log(ufo_sightings)
// });

// // Append the data. Is this extra???
// data.forEach(function(ufo_sightings) {
//     console.log();
//     var row = tbody.append('tr');
// })


// // var populate = (dataInput) => {
// //     dataInput.forEach(function(ufo_sightings) => {
// //         var row = d3.select('tbody').append('tr');
// //         columns.forEach(column => row.append('td').text(ufo_sightings[column]))
// //     });
// // }

// // YOUR CODE HERE!
// button.on("click", function() {
//     tbody.html("");

// function buildTable(data){
//     tbody.html("");
//     data.forEach((dataRow) => {
//         let row = tbody.append('tr');
//         Object.values(datarow).forEach((val) => {
//             let cell = row.append('td');
//             cell.text(val);
//         });
//     })
// }

