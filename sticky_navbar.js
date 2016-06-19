$(document).ready(function(){
    var origOffsetY = $('.menu').offset().top;
  
    function scroll() {
        if ($(window).scrollTop() >= origOffsetY) {
            $('.menu').addClass('navbar-fixed-top');
            var padding_top_value = $('.menu').height() + "px";
            console.log(padding_top_value);
            $('.content').css('padding-top', padding_top_value);
        } else {
            $('.menu').removeClass('navbar-fixed-top');
            $('.content').css('padding-top', 0);
        }
      }
      document.onscroll = scroll;
});