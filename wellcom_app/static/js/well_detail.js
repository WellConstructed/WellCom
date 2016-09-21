$(document).ready(function() {
    $(".drop_content").hide();
    $(".drop_header").click(function() {
        var $next = $(this).next(".drop_content")
        $(".drop_content").not($next).slideUp();
        $next.slideToggle(300);
    });
});


$('#water_test').click( function(){
    $(this).find('i').toggleClass('fa fa-chevron-right fa-fw').toggleClass('fa fa-chevron-down fa-fw');
    $('#updates').find('i').removeClass('fa fa-chevron-down fa-fw').addClass('fa fa-chevron-right fa-fw')
});

$('#updates').click( function(){
    $(this).find('i').toggleClass('fa fa-chevron-right fa-fw').toggleClass('fa fa-chevron-down fa-fw');
    $('#water_test').find('i').removeClass('fa fa-chevron-down fa-fw').addClass('fa fa-chevron-right fa-fw')
  });
