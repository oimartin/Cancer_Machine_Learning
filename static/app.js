console.log("I am working")

function optionChanged(newPlace){
    thisPlace = stateNames.find(d => d.State == newPlace);
    year = d3.select("#selDataset").property("value");
  } 

function init() {
 
  d3.json("/places").then((placeNames) => {
    console.log(placeNames)
    var i;
    for (i =0; i < placeNames.length; i++) {
      place = placeNames[i];
      d3.select("#selDataset")  
        .append("option")
        .text(place)
        .property("value", place);
        console.log(place)

    };
  }); 
 
}

init();

// function builCharts() {
  var url = [10,15,30,25,50,26,7]

// d3.json(url).then(function(data) {
//   console.log(data);
// });
  
//     d3.json(url).then(function(pollution) {

// Create the Traces
var trace1 = {
  x: ["CO","Lead","NO2","Ozone","PM10","PM2_5","SO2"],
  y: url,
  mode: "markers",
  type: "Bar",
  name: "Pollutants",
  marker: {
    color: "#2077b4",
    symbol: "hexagram"
  }
};

// Create the data array for the plot
var pollution = [trace1]

// Define the plot layout
var layout = {
  title: "State Pollution",
  xaxis: { title: "Pollutants" },
  yaxis: { title: "Parts Per Million" }
};

// Plot the chart to a div tag with id "plot"
Plotly.newPlot("Pollution_Plot", data, layout);

buildPlot();