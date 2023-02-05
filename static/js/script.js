

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
      $('.text-label h2:last-of-type').css('font-size', '1em')
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
      $('.text-label h2:last-of-type').css('font-size', '0.9em')
      shrink = false;
      
    }
    
  });
  

  // User Form input
  $("#userform div input").attr("class", "form-control");
  $("#userform div select").attr("class", "role-select rounded");
  
  // user client side validation for password

  $('#id_password1').focus(function () { 
    $('#userform-submit').attr('disabled', 'true');
  });

  // Password validation using regex
  $('#id_password1').keyup(function () { 
    const password_pattern = /(?=.*\d)(?=.*[a-z]).{8,}/i;

    if ($(this).val().match(password_pattern)) {
      console.log('yep')
    } else {
      console.log('nope')
    }
  });
  $('#fas').hide();
  $('#id_password2').keyup(function () { 
    if ($('#id_password1').val() == $('#id_password2').val()) {
      $('#userform-submit').removeAttr('disabled');
      $('#fas').hide();
    } else  {
      $('#userform-submit').attr('disabled', 'true');
      $('#fas').show();
    }
  });
});



// Dashboard Graph
$('.dashboard').ready(function () {
  const data = {
    labels: [
      'Green',
      'Blue',
      'Dark'
    ],
    datasets: [{
      label: 'My First Dataset',
      data: [300, 50, 100],
      backgroundColor: [
        '#1CDCB0',
        '#33A3EE',
        '#0E074D'
      ],
      hoverOffset: 4
    }]
  };

  const mychart = document.getElementById("myChart");
  new Chart(mychart, {
    type: 'doughnut',
    data: data,
  });
});