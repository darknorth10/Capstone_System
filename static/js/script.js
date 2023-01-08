$(document).ready(function() {
  var shrink = false;
  
  $('#shrink').click(function() {
    
    if (shrink == false) {
      $('.sidenav').css('width', "60px");
      $('.sidenav-menu li span').hide();
      $('.sidenav-menu li i').css("font-size", "0.8rem");
      $('.sidenav-menu li i').css("margin-bottom", "5px");
      $('#shrink').css('transform', 'rotate(180deg)');
      shrink = true;
    } else {
      $('.sidenav').css('width', "210px");
      setTimeout(function() {
        $('.sidenav-menu li span').show();
      }, 500);
      $('.sidenav-menu li i').css("font-size", "0.7rem");
      $('#shrink').css('transform', 'rotate(0deg)');
      shrink = false;
    }
    
  })
});

