$(document).ready(function() {
    $(".drop_content").hide();
    $(".drop_header").click(function() {
        var $next = $(this).next(".drop_content");
        $(".drop_content").not($next).slideUp();
        $next.slideToggle(500);
        $(this).toggleClass('exp');
    });
});
