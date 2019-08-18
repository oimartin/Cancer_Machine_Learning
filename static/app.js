console.log("I am working")

function optionChanged(newPlace){
    thisPlace = stateNames.find(d => d.State == newPlace);
    state = d3.select("#selState").property("value");
  } 
function init() {
 
  d3.json("/places").then((placeNames) => {
    gender();
    race();
    year();
    pollutant();
    console.log(placeNames)
    var i;
    for (i =0; i < placeNames.length; i++) {
      place = placeNames[i];
      d3.select("#selState")  
        .append("option")
        .text(place)
        .property("value", place);
        console.log(place)

    };
  }); 
}

function gender() {
  d3.json("/genders").then((genderNames) => {
  console.log(genderNames)
  var i;
  for (i=0; i < genderNames.length; i++) {
    gender = genderNames[i];
    d3.select("#selGender")
      .append("option")
      .text(gender)
      .property("value", gender);
      console.log(gender)
    };
  });
}

function race() {
  d3.json("/races").then((raceNames) => {
  console.log(raceNames)
  var i;
  for (i=0; i < raceNames.length; i++) {
    race = raceNames[i];
    d3.select("#selRace")
      .append("option")
      .text(race)
      .property("value", race);
      console.log(race)
    };
  });
}

function year() {
  d3.json("/year").then((yearNames) => {
  console.log(yearNames)
  var i;
  for (i=0; i < yearNames.length; i++) {
    year = yearNames[i];
    d3.select("#selYear")
      .append("option")
      .text(year)
      .property("value", year);
      console.log(year)
    };
  });
}

function cancer() {
  d3.json("/cancer").then((cancerNames) => {
  console.log(cancerNames)
  var i;
  for (i=0; i < cancerNames.length; i++) {
    cancer = cancerNames[i];
    d3.select("#selCancer")
      .append("option")
      .text(cancer)
      .property("value", cancer);
      console.log(cancer)
    };
  });
}

function pollutant() {
  d3.json("/pollutant").then((pollutantNames) => {
  console.log(pollutantNames)
  var i;
  for (i=0; i < pollutantNames.length; i++) {
    pollutant = pollutantNames[i];
    d3.select("#selPollutant")
      .append("option")
      .text(pollutant)
      .property("value", pollutant);
      console.log(pollutant)
    };
  });
}

function displayResults() {
  console.log("I'm running")
  // 1. get values of dropdowns
    state = d3.select("#selState").node().value;
    gender = d3.select("#selGender").node().value;
    race = d3.select("#selRace").node().value;
    year = d3.select("#selYear").node().value;
    d3.json("/api/"+state+"/"+race+"/"+year+"/"+gender).then((d) => {
      console.log(d)
      div = d3.select("#displayResults")
      div.text(d.laryanx)
    })
  }

  function displayResults() {
    console.log("I'm running")
    // 1. get values of dropdowns
      state = d3.select("#selState").node().value;
      gender = d3.select("#selGender").node().value;
      race = d3.select("#selRace").node().value;
      year = d3.select("#selYear").node().value;
      div = d3.select("#displayResults").text("");
      d3.json("/api/"+state+"/"+race+"/"+year+"/"+gender).then((d) => {
        console.log(d)
        div.append("p").text("Larynx: " + d.Larynx)
        div.append("p").text("Lung: " + d.Lung)
        div.append("p").text("Nasal: " + d.Nasal)
        div.append("p").text("Trachea: " + d.Trachea)
      })
    }
  init();

init();


