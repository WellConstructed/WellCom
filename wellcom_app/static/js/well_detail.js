$(document).ready(function() {
    $(".drop_content").hide();
    $(".drop_header").click(function() {
        var $next = $(this).next(".drop_content");
        $(".drop_content").not($next).slideUp();
        $next.slideToggle(500);
        $(this).toggleClass('exp');
    });
});


$('#water_test').click( function(){
    $(this).find('i').toggleClass('fa fa-chevron-right fa-fw').toggleClass('fa fa-chevron-down fa-fw');
});

$('#updates').click( function(){
    $(this).find('i').toggleClass('fa fa-chevron-right fa-fw').toggleClass('fa fa-chevron-down fa-fw');
});
