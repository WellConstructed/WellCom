$(document).ready(function() {
  $('#all_well_data').dataTable();
});

$(document).ready(function($) {
    $(".clickable-row").click(function() {
        window.document.location = $(this).data("href");
    });
});

$(window).scroll(function() {
   if($(window).scrollTop() + $(window).height() == $(document).height()) {
       console.log("bottom!");
       $(document).find("i").toggleClass("fa fa-arrow-circle-down fa-2x").toggleClass("fa fa-arrow-circle-up fa-2x");
   }
});
