// @TODO: YOUR CODE HERE!

// Set SVG Width & Height
var svgWidth = 960;
var svgHeight = 620;

// Set SVG Margins
var margin = {
    top: 20,
    right: 40,
    bottom: 200,
    left: 100
};

// Use the margins to fit chart
var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// Append Div Class Chart to Scatter Element
var svg = d3.select('#scatter')
    .append('svg')
    .attr('width', svgWidth)
    .attr('height', svgHeight);



