// Assigns Id: 'header-not-at-top' to <header></header> when the position is not at top:0
window.addEventListener('scroll', function() {
    var header = document.querySelector('header');
    if (window.scrollY > 0) {
        header.setAttribute('id', 'header-not-at-top');
    } else {
        header.removeAttribute('id');
    }
});