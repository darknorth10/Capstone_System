

$(document).ready(function() {

  var shrink = false;
  
  $('#shrink').click(function() {
    
    if (shrink == false) {
      $('.sidenav').css('width', "60px");
      $('.sidenav').css('justify-content', "center");
      $('.sidenav-menu li span').hide();
      $('.sidenav-menu').css('gap', '15px');
      $('.sidenav-menu li i').css("font-size", "0.8rem");
      $('.sidenav-menu li i').css("margin-bottom", "5px");
      $('#navlogo').css('visibility', 'hidden');
      $('#shrink').css('transform', 'rotate(180deg)');
      $('.left-symbol').css('width', '30%')
      $('.text-label h2:last-of-type').css('font-size', '1rem')
      shrink = true;
    } else {
      $('.sidenav').css('width', "210px");
      setTimeout(function() {
        $('.sidenav-menu li span').show();
      }, 500);
      $('.sidenav-menu li i').css("font-size", "0.7rem");
      $('#navlogo').css('visibility', 'visible');
      $('.sidenav-menu').css('gap', '5px');
      $('#shrink').css('transform', 'rotate(0deg)');
      $('.left-symbol').css('width', '20%')
      $('.text-label h2:last-of-type').css('font-size', '0.9rem')
      shrink = false;
      
    }
    
  })
  
  
});

