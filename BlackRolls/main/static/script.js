$(document).ready(function() {
    $('footer').fadeOut('slow');
});

$(window).scroll(function() {    
    var scroll = $(window).scrollTop();

    if (scroll >= 50) {
        $('.header-warning').fadeOut('slow');
    } else {
        $('.header-warning').fadeIn('slow');
    }

    if (scroll >= 0.4 * $(window).height()) {
        $('footer').fadeIn('slow');
    } else {
        $('footer').fadeOut('slow');
    }
});