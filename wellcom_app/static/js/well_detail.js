$(document).ready(function() {
    $(".drop_content").hide();
    $(".drop_header").click(function() {
        var $next = $(this).next(".drop_content");
        $(".drop_content").not($next).slideUp();
        $next.slideToggle(300);
      div.addEventListener('click', function(){
        if(open){
          icon.className = 'fa fa-arrow-down';
        } else{
          icon.className = 'fa fa-arrow-down open';
        }
        open = !open;
    });
});
});
