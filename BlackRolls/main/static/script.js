$(document).ready(function() {
    $('footer').fadeOut('slow');
});

$(window).scroll(function() {    
    var scroll = $(window).scrollTop();    
    if (scroll >= 0.4 * $(window).height()) {
        $('footer').fadeIn('slow');
    } else {
        $('footer').fadeOut('slow');
    }
});