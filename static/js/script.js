
// Dashboard Top Selling Graph
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

// document is ready and loaded
$(document).ready(function() {

  var shrink = false;
  
  $('#shrink').click(function() {
    
    if (shrink == false) {
      $('.sidenav').css('width', "60px");
      $('.sidenav').css('justify-content', "center");
      $('.sidenav-menu li span').hide();
      //$('.sidenav-menu').css('gap', '15px');
      $('.sidenav-menu li i').css("font-size", "0.8rem");
      $('.sidenav-menu li i').css("margin-bottom", "5px");
      // $('#navlogo').css('visibility', 'hidden');
      $('#navlogo').hide()
      $('#shrink').css('transform', 'rotate(180deg)');
      $('.left-symbol').css('width', '30%')
      $('.text-label h2:last-of-type').css('font-size', '1em')
      shrink = true;
    } else {
      $('.sidenav').css('width', "18%");
      setTimeout(function() {
        $('.sidenav-menu li span').show();
      }, 500);
      $('.sidenav-menu li i').css("font-size", "0.7rem");
      $('.sidenav').css('justify-content', "space-evenly");
      $('#navlogo').css('visibility', 'visible');
      // $('#navlogo').css('visibility', 'visible');
      $('#navlogo').show()
      //$('.sidenav-menu').css('gap', '15px');
      $('#shrink').css('transform', 'rotate(0deg)');
      $('.left-symbol').css('width', '20%')
      $('.text-label h2:last-of-type').css('font-size', '0.9em')
      shrink = false;
      
    }
    
  });
  
  // Alert Function
  $(document).ready(function () {
    if ( $("#alert_box h5").text() != "" ) {
      $("#alert_box").css('top', '5%'); // show the alert box

      setTimeout(function () { // hide the alert box
        $("#alert_box").css('top', '-20%');
      }, 3000);
    }

  });
  // User Form input class
  $("#userform div input").attr("class", "form-control shadow-inner p-2");
  // Edit user input class
  $("#userform-edit div input").attr("class", "form-control shadow-inner active");
  // For Select Role class
  $("#userform div select").attr("class", "role-select rounded");
  $("#userform-edit div select").attr("class", "role-select rounded");
  
  
  // user client side validation for password

  $('#id_password1').focus(function () { 
    $('#userform-submit').attr('disabled', 'true');
  });

  // Password validation using regex
  $('#fas1').hide();
  $('#id_password1').keyup(function () { 
    const password_pattern = /(?=.*\d)(?=.*[a-z]).{8,}/i;

    if ($(this).val().match(password_pattern)) {
      $('#fas1').removeAttr('class');
      $('#fas1').attr('class', 'fa-solid fa-circle-check trailing');
      $('#fas1').css('color', 'rgb(51, 204, 158)');
    } else {
      $('#fas1').show();
      $('#fas1').removeAttr('class');
      $('#fas1').css('color', 'rgb(220, 71, 66)');
      $('#fas1').attr('class', 'fas fa-exclamation-circle trailing')
    }
  });

  // validation indicator in confirm password
  $('#fas').hide();
  $('#id_password2').keyup(function () { 
    if ($('#id_password1').val() == $('#id_password2').val()) {
      $('#userform-submit').removeAttr('disabled');
      $('#fas').removeAttr('class');
      $('#fas').attr('class', 'fa-solid fa-circle-check trailing');
      $('#fas').css('color', 'rgb(51, 204, 158)');
    } else  {
      $('#userform-submit').attr('disabled', 'true');
      $('#fas').show();
      $('#fas').removeAttr('class');
      $('#fas').css('color', 'rgb(220, 71, 66)');
      $('#fas').attr('class', 'fas fa-exclamation-circle trailing');
    }
  });
  
  // close the alert window
  $('#close_alert').click(function (e) { 
    e.preventDefault();
    $('#alert_box').css('top', '-20%');
  });

  //  User form using ajax request / preventing from reloading when submitting
  $('#userform').submit(function (e) { 
    e.preventDefault();
    
    //ajaxx request
    $.ajax({
      type: "post",
      url: "",
      data: $(this).serialize(),
      success: function (response) {

        if (response.success) {
          $('#adduser_close').click() // close the form
          $('#adduser_reset').click() // reset the form
          location.reload();

        }
        
        else { // alert the validation error
  
          var usernameErrExist = response.errors.hasOwnProperty('username');
          var pwdErrExist = response.errors.hasOwnProperty('password2');
          var errormessage;

          // check if username err exist in the object
          if (usernameErrExist && !pwdErrExist) {
            // check if username err is only 1
            if (response.errors.username.length == 1) {
              errormessage = response.errors.username
            }
          } else if(pwdErrExist && !usernameErrExist) { // Check if pwd err exist in the object
            if (response.errors.password2.length == 1) { // Check if password err is only 1
              errormessage = response.errors.password2;
            } else if (response.errors.password2.length == 2) {
              errormessage = response.errors.password2[0] + "\n" + response.errors.password2[1];
            }
          } else if (usernameErrExist && pwdErrExist) {
            if (response.errors.password2.length == 2 && response.errors.username.length == 1) {
              errormessage = response.errors.username + "\n" + response.errors.password2[0] + "\n" + response.errors.password2[1];
            } else if(response.errors.password2.length == 1 && response.errors.username.length == 1) {
              errormessage = response.errors.username + "\n" + response.errors.password2;
            }
          } else {
            errormessage = response.errors
          }
          
          alert(errormessage);
        }
        
      }
    });
  });

  // Product management

  // form validation for add product
  $('#id_category').change(function () { 
    if ($(this).val() == "Porcelain Tiles" || $(this).val() == "Ceramic Tiles") {
      $("#id_product_size option[value='N/A']").attr('disabled', 'disabled');
      $("#id_product_size option[value='20 x 20']").removeAttr('disabled');
      $("#id_product_size option[value='30 x 30']").removeAttr('disabled');
      $("#id_product_size option[value='60 x 30']").removeAttr('disabled');
      $("#id_product_size").val('').change();
    } else {

     $("#id_product_size option[value='N/A']").removeAttr('disabled');
     $("#id_product_size option[value='20 x 20']").attr('disabled', 'disabled');
     $("#id_product_size option[value='30 x 30']").attr('disabled', 'disabled');
     $("#id_product_size option[value='60 x 30']").attr('disabled', 'disabled');
     $("#id_product_size").val('').change();
 
    }
  });



  // Ajax add product
  $("#add_prod_form").submit(function(e) {
    e.preventDefault();
    e.stopImmediatePropagation();
    var formData = new FormData(this);

    $.ajax({
      type: "post",
      url: window.location.href + "add_new_product/",
      data: formData,
      success: function (response) {
        if (response.success) {
          location.reload();
        } else {
          alert(response.errors.__all__ + "\n" + response.errors.price + " in price");
        }
      },
      cache: false,
      contentType: false,
      processData: false
    });
  
  });
  
  $("#id_current_stock").keyup(function () { 
    $("#curr_stock").text($(this).val())
  });

  $("#conf_addStock").click(function () { 
    $("#addstock_form").submit();
  });

  
  // Customer Profile
  $("#regcust").click(function () { 
    
    $("#add_cust_submit").click();
  });

});



