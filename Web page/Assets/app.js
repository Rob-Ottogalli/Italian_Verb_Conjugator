let inputField = d3.select("#input-form")
let outputField = d3.select("#endregionexampleFormControlTextarea1")

// Function to handle input change
function handleChange(event) {
    // grab the value of the input field
    var inputValue = d3.event.target.value;
  
    // clear the existing output
    outputField.text("");
  
    // Set the output text to the input string
    outputField.text(inputValue);

  }
  
  // Attach an event to detect changes to the input field.
  inputField.on("change", handleChange);