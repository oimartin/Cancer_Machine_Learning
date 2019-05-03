function buildPlot() {
    var url = `https://www.quandl.com/api/v3/datasets/WIKI/AMZN.json?start_date=2016-10-01&end_date=2017-10-01&api_key=${apiKey}`;
  
    d3.json(url).then(function(pollution) {

// Create the Traces
var trace1 = {
  x: pollution.year,
  y: pollution.CO,
  mode: "markers",
  type: "scatter",
  name: "CO",
  marker: {
    color: "#2077b4",
    symbol: "hexagram"
  }
};

var trace2 = {
  x: pollution.year,
  y: pollution.Lead,
  mode: "markers",
  type: "scatter",
  name: "Lead",
  marker: {
    color: "orange",
    symbol: "diamond-x"
  }
};

var trace3 = {
  x: pollution.year,
  y: pollution.NO2,
  mode: "markers",
  type: "scatter",
  name: "NO2",
  marker: {
    color: "rgba(156, 165, 196, 1.0)",
    symbol: "cross"
  }
};
var trace4 = {
    x: pollution.year,
    y: pollution.Ozone,
    mode: "markers",
    type: "scatter",
    name: "Ozone",
    marker: {
      color: "rgba(156, 165, 196, 1.0)",
      symbol: "cross"
    }
  };

var trace5 = {
    x: pollution.year,
    y: pollution.PM10,
    mode: "markers",
    type: "scatter",
    name: "PM10",
    marker: {
      color: "rgba(156, 165, 196, 1.0)",
      symbol: "cross"
    }
  };

var trace6 = {
    x: pollution.year,
    y: pollution.PM2.5,
    mode: "markers",
    type: "scatter",
    name: "PM2.5",
    marker: {
      color: "rgba(156, 165, 196, 1.0)",
      symbol: "cross"
    }
  };
var trace7 = {
    x: pollution.year,
    y: pollution.SO2,
    mode: "markers",
    type: "scatter",
    name: "SO2",
    marker: {
      color: "rgba(156, 165, 196, 1.0)",
      symbol: "cross"
    }
  };

// Create the data array for the plot
var pollution = [trace1, trace2, trace3, trace4, trace5, trace6, trace7];

// Define the plot layout
var layout = {
  title: "Pollution",
  xaxis: { title: "Year" },
  yaxis: { title: "Parts Per Million" }
};

// Plot the chart to a div tag with id "plot"
Plotly.newPlot("Pollution_Plot", data, layout);

buildPlot();
