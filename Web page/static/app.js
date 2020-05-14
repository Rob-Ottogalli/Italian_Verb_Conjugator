//-------------------------------------------
// Function to handle typed input
//-------------------------------------------

const inputField = d3.select("#input-form");
const outputField = d3.select(".output-text");

// Function to handle input change
function verbToTable(event) {
    // grab the value of the input field
    let verb = d3.event.target.value;
  
    // clear the existing output
    outputField.text("");
  
    // Set the output text to the input string
    outputField.text(verb);

}

// Attach an event to detect changes to the input field.
inputField.on("change", verbToTable);

//-------------------------------------------
// Function to handle person dropdown
//-------------------------------------------

const personDropdown = d3.select("#inputGroupSelect01");
const personOutput = d3.select(".output-person");

function personToTable(event) {
  let person = d3.event.target.value;

  if (person === "Choose person...") {
    personOutput.text("");
  }
  else {
    personOutput.text("");
    personOutput.text(person);
  }
}

personDropdown.on("change", personToTable);


//-------------------------------------------
// Function to handle mood dropdown
//-------------------------------------------

const moodDropdown = d3.select("#inputGroupSelect02");
const moodOutput = d3.select(".output-mood");

function moodToTable(event) {
  let mood = d3.event.target.value;

  if (mood === "Choose verb mood...") {
    moodOutput.text("");
  }
  else {
    moodOutput.text("");
    moodOutput.text(mood);
  }

  setTenseMenu(mood);
}

moodDropdown.on("change", moodToTable);

//-------------------------------------------
// Function to modify tense/aspect dropdown
//-------------------------------------------
const tenseDropdown = d3.select("#inputGroupSelect03");
const tenseOutput = d3.select(".output-tense");

function setTenseMenu(mood) {
  // Set empty list to hold dropdown menu options
  let listOptions = [];

  // The tense/aspect menu options will populate 
  // from the following lists
  // depending on mood selected from previous dropdown menu.
  if (mood === "indicative") {
    listOptions = ["Choose tense/aspect...", "present", "imperfect", 
                  "past absolute", "future simple", "future perfect",
                  "present perfect", "pluperfect", "remote pluperfect"];
  }
  else if (mood === "subjunctive") {
    listOptions = ["Choose tense/aspect...", "present", "imperfect", 
                  "present perfect", "pluperfect"];
  }
  else if (mood === "conditional") {
    listOptions = ["Choose tense/aspect...", "present", "perfect"];
  }
  else if (mood === "imperative") {
    listOptions = ["Choose tense/aspect...", "--"];
  }

  // populate menu options into the dropdown menu.
  // Set variable to hold selection of dropdown tag and data
  var selection = tenseDropdown.selectAll("select").data(listOptions);

  // Update new data and merge old
  selection.enter()
    .append("option")
    .merge(selection)
    .html(function (d) {
      return d;
    });
  
  // Delete unnecessary elements
  selection.exit().remove();
}

//-------------------------------------------
// Function to print tense dropdown to table
//-------------------------------------------


function tenseToTable(event) {
  let tense = d3.event.target.value;

  if (tense === "Choose tense/aspect...") {
    tenseOutput.text("");
  }
  else {
    tenseOutput.text("");
    tenseOutput.text(tense);
  }

}

tenseDropdown.on("change", tenseToTable);