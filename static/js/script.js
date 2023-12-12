// Listen for the scroll event
window.addEventListener('scroll', function() {

    // Select the header element
    var header = document.querySelector('header');

    // Check if the scroll position is greater than 50 pixels
    if (window.scrollY > 50) {
        // If true, add 'sticky-top' class to make the header sticky
        header.setAttribute('class', 'sticky-top');
    } else {
        // If false, remove the class to position the header on top
        header.removeAttribute('class');
    }
});