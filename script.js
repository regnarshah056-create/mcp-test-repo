// Add event listener to the button
// Since Node.js does not have a document object, we will use a library like jsdom to simulate a browser environment
const jsdom = require('jsdom');
const { JSDOM } = jsdom;
const dom = new JSDOM(`<!DOCTYPE html><html><body><button>Click me</button></body></html>`);
const document = dom.window.document;
const button = document.querySelector('button');
button.addEventListener('click', () => {
    // Add functionality to the button click event
    console.log('Button clicked');
});