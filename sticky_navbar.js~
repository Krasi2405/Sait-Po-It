$(document).ready(function(){
    var origOffsetY = $('.menu').offset().top;

    function scroll() {
        if ($(window).scrollTop() >= origOffsetY) {
            $('.menu').addClass('navbar-fixed-top');
            $('.content').css('padding-top', $('nav').height);
        } else {
            $('.menu').removeClass('navbar-fixed-top');
            $('.content').css('padding-top', 0);
        }
      }
      document.onscroll = scroll;
});
