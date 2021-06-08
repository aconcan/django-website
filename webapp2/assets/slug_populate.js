const titleInput = document.querySelector('input[name=title]');
const slugInput = document.querySelector('input[name=slug]');

// Specifying the behaviour of the arrow function 
const slugify = (val) => {
    return val.toString().toLowerCase().trim()
        // Using regex to do hyphen replacements
        .replace(/&/g, '-and-') // Replace '&'
        .replace(/[\s\W-]+/g, '-') // Replace spaces and non-word chars w dashes
};

// Set value attribute of slug to the value returned from slugify
titleInput.addEventListener('keyup', (e) => {
    slugInput.setAttribute('value', slugify(titleInput.value));
});
