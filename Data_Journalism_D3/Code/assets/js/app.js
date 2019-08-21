//SVG dimensions set for width, height and borders
//set svg height and width
var svgWidth = 980;
var svgHeight = 640;

//set borders in svg
var margin = {
    top: 20,
    right: 40,
    bottom: 100,
    left: 100
};

//Chart height and width
var width = svgWidth - margin.right - margin.left;
var height = svgHeight - margin.top - margin.bottom;

//Append div classed chart to the scatter element
var chart = d3.select("#scatter").append("div").classed("chart", true);

// Append SVG element to the chart 
// for width and height
var svg = chart.append("svg")
    .attr("width", svgWidth)
    .attr("height", svgHeight);

//Append SVG group
var chartGroup = svg.append("g")
    .attr("transform", `translate(${margin.left}, ${margin.top})`);

//Identify initial parameters
var selectedXAxis = "poverty";
var selectedYAxis = "healthcare";

//Function used for updating x-scale var upon clicking on axis label
function xScale(censusData, selectedXAxis) {
    //create scales
    var xLinearScale = d3.scaleLinear()
        .domain([d3.min(censusData, d => d[selectedXAxis]) * 0.8,
            d3.max(censusData, d => d[selectedXAxis]) * 1.2])
        .range([0, width]);

    return xLinearScale;
}

//Function used for updating y-scale var upon clicking on axis label
function yScale(censusData, selectedYAxis) {
    //create scales
    var yLinearScale = d3.scaleLinear()
        .domain([d3.min(censusData, d => d[selectedYAxis]) * 0.8,
            d3.max(censusData, d => d[selectedYAxis]) * 1.2])
        .range([height, 0]);

    return yLinearScale;
}

//Function used for updating xAxis var upon click on axis label
function renderAxesX(newXScale, xAxis) {
    var bottomAxis = d3.axisBottom(newXScale);

    xAxis.transition()
        .duration(500)
        .call(bottomAxis);

    return xAxis;
}

//Function used for updating yAxis var upon click on axis label
function renderAxesY(newYScale, yAxis) {
    var leftAxis = d3.axisLeft(newYScale);

    yAxis.transition()
        .duration(500)
        .call(leftAxis);

    return yAxis;
}

// Function used for updating circles group 
// Transitions to new circles for change in x axis or y axis
function renderCircles(circlesGroup, newXScale, selectedXAxis, newYScale, selectedYAxis) {

    circlesGroup.transition()
        .duration(500)
        .attr("cx", data => newXScale(data[selectedXAxis]))
        .attr("cy", data => newYScale(data[selectedYAxis]));

    return circlesGroup;
}

// Function used for updating state labels 
// Transitions to a new variable selection
function renderText(textGroup, newXScale, selectedXAxis, newYScale, selectedYAxis) {

    textGroup.transition()
        .duration(500)
        .attr("x", d => newXScale(d[selectedXAxis]))
        .attr("y", d => newYScale(d[selectedYAxis]));

    return textGroup;
}
//Function to stylize x-axis values for tooltips
function styleX(value, selectedXAxis) {

    //Stylize based on variable selected poverty percentage
    if (selectedXAxis === 'poverty') {
        return `${value}%`;
    }
    //Household income in dollars
    else if (selectedXAxis === 'income') {
        return `$${value}`;
    }
    //Age (number)
    else {
        return `${value}`;
    }
}

//Function used for updating circles' group with new tooltip
function updateToolTip(selectedXAxis, selectedYAxis, circlesGroup) {

    //Select x label
    
    if (selectedXAxis === 'poverty') {
        var xLabel = "Poverty:";
    }
    
    else if (selectedXAxis === 'income') {
        var xLabel = "Median Income:";
    }
    
    else {
        var xLabel = "Age:";
    }

    // Select y label
    // Percentage lacking healthcare
    if (selectedYAxis === 'healthcare') {
        var yLabel = "No Healthcare:"
    }
    // Percentage Obese
    else if (selectedYAxis === 'obesity') {
        var yLabel = "Obesity:"
    }
    // Smoking percentage
    else {
        var yLabel = "Smokers:"
    }

    // Create tooltip
    var toolTip = d3.tip()
        .attr("class", "d3-tip")
        .offset([0,0])
        .html(function(d) {
            return (`${d.state}<br>${xLabel} ${styleX(d[selectedXAxis], selectedXAxis)}<br>${yLabel} ${d[selectedYAxis]}%`);
        });

    circlesGroup.call(toolTip);

    //add events
    circlesGroup.on("mouseover", toolTip.show)
    .on("mouseout", toolTip.hide);

    return circlesGroup;
}

// Retrieve csv data
d3.csv("./assets/data/data.csv").then(function(censusData) {

    console.log(censusData);

    // Parse data
    censusData.forEach(function(data) {
        data.obesity = +data.obesity;
        data.income = +data.income;
        data.smokes = +data.smokes;
        data.age = +data.age;
        data.healthcare = +data.healthcare;
        data.poverty = +data.poverty;
    });

    // Create first linear scales
    var xLinearScale = xScale(censusData, selectedXAxis);
    var yLinearScale = yScale(censusData, selectedYAxis);

    // Create initial axis functions
    var bottomAxis = d3.axisBottom(xLinearScale);
    var leftAxis = d3.axisLeft(yLinearScale);

    // Append x axis
    var xAxis = chartGroup.append("g")
        .classed("x-axis", true)
        .attr("transform", `translate(0, ${height})`)
        .call(bottomAxis);

    // Append y axis
    var yAxis = chartGroup.append("g")
        .classed("y-axis", true)
        .call(leftAxis);

    // Append initial circles
    var circlesGroup = chartGroup.selectAll("circle")
        .data(censusData)
        .enter()
        .append("circle")
        .classed("stateCircle", true)
        .attr("cx", d => xLinearScale(d[selectedXAxis]))
        .attr("cy", d => yLinearScale(d[selectedYAxis]))
        .attr("r", 12)
        .attr("opacity", ".8");

    // Append initial text
    var textGroup = chartGroup.selectAll(".stateText")
        .data(censusData)
        .enter()
        .append("text")
        .classed("stateText", true)
        .attr("x", d => xLinearScale(d[selectedXAxis]))
        .attr("y", d => yLinearScale(d[selectedYAxis]))
        .attr("dy", 3)
        .attr("font-size", "10px")
        .text(function(d){return d.abbr});

    // Create group for 3 x-axis labels
    var xLabelsGroup = chartGroup.append("g")
        .attr("transform", `translate(${width / 2}, ${height + 20 + margin.top})`);

    var povertyLabel = xLabelsGroup.append("text")
        .classed("aText", true)
        .classed("active", true)
        .attr("x", 0)
        .attr("y", 20)
        .attr("value", "poverty")
        .text("In Poverty (%)");

    var ageLabel = xLabelsGroup.append("text")
        .classed("aText", true)
        .classed("inactive", true)
        .attr("x", 0)
        .attr("y", 40)
        .attr("value", "age")
        .text("Age (Median)")

    var incomeLabel = xLabelsGroup.append("text")
        .classed("aText", true)
        .classed("inactive", true)
        .attr("x", 0)
        .attr("y", 60)
        .attr("value", "income")
        .text("Household Income (Median)")

    // Create group for 3 y-axis labels
    var yLabelsGroup = chartGroup.append("g")
        .attr("transform", `translate(${0 - margin.left/4}, ${(height/2)})`);

    var healthcareLabel = yLabelsGroup.append("text")
        .classed("aText", true)
        .classed("active", true)
        .attr("x", 0)
        .attr("y", 0 - 20)
        .attr("dy", "1em")
        .attr("transform", "rotate(-90)")
        .attr("value", "healthcare")
        .text("No Healthcare (%)");

    var smokesLabel = yLabelsGroup.append("text")
        .classed("aText", true)
        .classed("inactive", true)
        .attr("x", 0)
        .attr("y", 0 - 40)
        .attr("dy", "1em")
        .attr("transform", "rotate(-90)")
        .attr("value", "smokes")
        .text("Smoking (%)");

    var obesityLabel = yLabelsGroup.append("text")
        .classed("aText", true)
        .classed("inactive", true)
        .attr("x", 0)
        .attr("y", 0 - 60)
        .attr("dy", "1em")
        .attr("transform", "rotate(-90)")
        .attr("value", "obesity")
        .text("Obese (%)");

    // UpdateToolTip function with data
    var circlesGroup = updateToolTip(selectedXAxis, selectedYAxis, circlesGroup);

    // x axis labels event listener
    xLabelsGroup.selectAll("text")
        .on("click", function() {
            // Get value of selection
            var value = d3.select(this).attr("value");

            // Check if value is same as current axis
            if (value != selectedXAxis) {

                // Replace selectedXAxis with value
                selectedXAxis = value;

                // Update x scale for new data
                xLinearScale = xScale(censusData, selectedXAxis);

                // Update x axis with transition
                xAxis = renderAxesX(xLinearScale, xAxis);

                // Update circles with new x values
                circlesGroup = renderCircles(circlesGroup, xLinearScale, selectedXAxis, yLinearScale, selectedYAxis);

                // Update text with new x values
                textGroup = renderText(textGroup, xLinearScale, selectedXAxis, yLinearScale, selectedYAxis);

                // Update tooltips with new info
                circlesGroup = updateToolTip(selectedXAxis, selectedYAxis, circlesGroup);

                // Change classes to change bold text
                if (selectedXAxis === "poverty") {
                    povertyLabel.classed("active", true).classed("inactive", false);
                    ageLabel.classed("active", false).classed("inactive", true);
                    incomeLabel.classed("active", false).classed("inactive", true);
                }
                else if (selectedXAxis === "age") {
                    povertyLabel.classed("active", false).classed("inactive", true);
                    ageLabel.classed("active", true).classed("inactive", false);
                    incomeLabel.classed("active", false).classed("inactive", true);
                }
                else {
                    povertyLabel.classed("active", false).classed("inactive", true);
                    ageLabel.classed("active", false).classed("inactive", true);
                    incomeLabel.classed("active", true).classed("inactive", false);
                }
            }
        });

    // y axis labels event listener
    yLabelsGroup.selectAll("text")
    .on("click", function() {
        // Get value of selection
        var value = d3.select(this).attr("value");

        // Check if value is same as current axis
        if (value != selectedYAxis) {

            // Replace selectedYAxis with value
            selectedYAxis = value;

            // Update y scale for new data
            yLinearScale = yScale(censusData, selectedYAxis);

            // Update x axis with transition
            yAxis = renderAxesY(yLinearScale, yAxis);

            // Update circles with new y values
            circlesGroup = renderCircles(circlesGroup, xLinearScale, selectedXAxis, yLinearScale, selectedYAxis);

            // Update text with new y values
            textGroup = renderText(textGroup, xLinearScale, selectedXAxis, yLinearScale, selectedYAxis)

            // Update tooltips with new info
            circlesGroup = updateToolTip(selectedXAxis, selectedYAxis, circlesGroup);

            // Change classes to change bold text
            if (selectedYAxis === "obesity") {
                obesityLabel.classed("active", true).classed("inactive", false);
                smokesLabel.classed("active", false).classed("inactive", true);
                healthcareLabel.classed("active", false).classed("inactive", true);
            }
            else if (selectedYAxis === "smokes") {
                obesityLabel.classed("active", false).classed("inactive", true);
                smokesLabel.classed("active", true).classed("inactive", false);
                healthcareLabel.classed("active", false).classed("inactive", true);
            }
            else {
                obesityLabel.classed("active", false).classed("inactive", true);
                smokesLabel.classed("active", false).classed("inactive", true);
                healthcareLabel.classed("active", true).classed("inactive", false);
            }
        }
    });
});