function generateOptions(id, minOptions, numOfOptions) { // don't leak
    var elm = document.getElementById(id), // get the select
        df = document.createDocumentFragment(); // create a document fragment to hold the options while we create them
    for (var i = minOptions; i <= numOfOptions; i++) { // loop, i like 42.
        var option = document.createElement('option'); // create the option element
        option.value = i; // set the value property
        option.appendChild(document.createTextNode(i)); // set the textContent in a safe way.
        df.appendChild(option); // append the option to the document fragment
    }
    elm.appendChild(df); // append the document fragment to the DOM. this is the better way rather than setting innerHTML a bunch of times (or even once with a long string)
}

var sqftLivingSlider = document.getElementById("sqftLiving");
var sqftLivingHTML = document.getElementById("sqftLivingValue");
sqftLivingHTML.innerHTML = sqftLivingSlider.value;

sqftLivingSlider.oninput = function () {
    sqftLivingHTML.innerHTML = this.value;
}

var sqftAboveSlider = document.getElementById("sqftAbove");
var sqftAboveHTML = document.getElementById("sqftAboveValue");
sqftAboveHTML.innerHTML = sqftAboveSlider.value;

sqftAboveSlider.oninput = function () {
    sqftAboveHTML.innerHTML = this.value;
}

var sqft15Slider = document.getElementById("sqft15");
var sqft15HTML = document.getElementById("sqft15Value");
sqft15HTML.innerHTML = sqft15Slider.value;

sqft15Slider.oninput = function () {
    sqft15HTML.innerHTML = this.value;
}

function resetForm() {
    document.getElementById('houseInputForm').reset();
    sqftLivingHTML.innerHTML = sqftLivingSlider.value;
    sqftAboveHTML.innerHTML = sqftAboveSlider.value;
    sqft15HTML.innerHTML = sqft15Slider.value;
}

generateOptions('noOfBedrooms', 0, 11)
generateOptions('view', 0, 4)
generateOptions('grade', 1, 13)