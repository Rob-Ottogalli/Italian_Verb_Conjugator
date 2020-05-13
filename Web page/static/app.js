//-------------------------------------------
// Function to handle typed input
//-------------------------------------------

const inputField = d3.select("#input-form");
const outputField = d3.select(".output-text");

// Function to handle input change
function verbToTable(event) {
    // grab the value of the input field
    let inputValue = d3.event.target.value;
  
    // clear the existing output
    outputField.text("");
  
    // Set the output text to the input string
    outputField.text(inputValue);

}

// Attach an event to detect changes to the input field.
inputField.on("change", verbToTable);

//-------------------------------------------
// Function to handle person dropdown
//-------------------------------------------

const personDropdown = d3.select("#inputGroupSelect01");
const personOutput = d3.select(".output-person");

function personToTable(event) {
  let inputValue = d3.event.target.value;
  personOutput.text("");
  personOutput.text(inputValue);
}

personDropdown.on("change", personToTable);


//-------------------------------------------
// Function to handle mood dropdown
//-------------------------------------------

const moodDropdown = d3.select("#inputGroupSelect02");
const moodOutput = d3.select(".output-mood");

function moodToTable(event) {
  let mood = d3.event.target.value;

  moodOutput.text("");
  moodOutput.text(mood);

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
  tenseDropdown
  .selectAll("select")
  .data(listOptions)
  .enter()
  .append("option")
  .html(function (d) {
    return d;
  });
}

//-------------------------------------------
// Function to handle mood dropdown
//-------------------------------------------


function tenseToTable(event) {
  let tense = d3.event.target.value;

  tenseOutput.text("");
  tenseOutput.text(tense);
}

tenseOutput.on("change", tenseToTable);