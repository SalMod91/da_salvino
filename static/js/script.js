// Assigns Class: 'sticky-top' to <header> when the position is not at top:0
window.addEventListener('scroll', function() {
    var header = document.querySelector('header');
    if (window.scrollY > 50) {
        header.setAttribute('class', 'sticky-top');
    } else {
        header.removeAttribute('class');
    }
});