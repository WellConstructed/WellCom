$(document).ready(function() {
  $('#all_well_data').dataTable();
});

$(document).ready(function($) {
    $(".clickable-row").click(function() {
        window.document.location = $(this).data("href");
    });
});


$(window).scroll(function(){
    $(".fixed").css("opacity", 0.6 - $(window).scrollTop() / 250);
  });

$(window).scroll(function(){
    $(".fix").css("opacity", 0.6 - $(window).scrollTop() / 250);
  });

var myElements = document.querySelector("#battery");

//   if (Well.batt_percent_charged >=75) {
//     myElements.style.color = #CB0000;
// }
