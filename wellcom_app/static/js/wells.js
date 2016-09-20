$(document).ready(function() {
  $('#all_well_data').dataTable();
});

$(document).ready(function($) {
    $(".clickable-row").click(function() {
        window.document.location = $(this).data("href");
    });
});
