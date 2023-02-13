
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
      $('.sidenav').css('width', "210px");
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
    $('#alert_box').css('top', '-10%');
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
          $("#alert_box").css('top', '5%'); // show the alert box
          $("#user-table").load(window.location.href + " #user-table") // load the user table with new data

            // alert will be hidden after 4 seconds
          setTimeout(function () {
            $("#alert_box").css('top', '-10%');
          }, 4000);

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

  $('#userform-edit').submit(function (e) { 
    e.preventDefault();
    
    $.ajax({
      type: "post",
      url: "",
      data: $(this).serialize(),
      success: function (response) {
        if (response.success) {
          $("#alert_box h5").text("Updated Successfully");
          $("#alert_box").css('top', '5%'); // show the alert box        

            // alert will be hidden after 4 seconds
          setTimeout(function () {
            $("#alert_box").css('top', '-10%');
          }, 3500);
        } else {
          alert("error");  
        }
      }
    });
  });

  // when activate button clicked
  $("#userstatusbtn a").on('click', function () {
    // selecting hidden id in the users table
    let userid = $(this).parent().parent().children().last().text();
    $('#user_id').val(userid);
    console.log(userid)

  });

  $("#userstatusbtn a").on('click', function () {
    // selecting hidden id in the users table
    let userid2 = $(this).parent().parent().children().last().text();
    $('#user_id').val(userid2);
    console.log(userid2)

  });

  // function for activating and deactivating the user
  function updateStatus() {
    // submitting hidden form to access object.id in the views.py
    $('#act-deact').submit(function (e) { 
      e.preventDefault();
      
      // ajax request
      $.ajax({
        type: "post",
        url: window.location.href + "edit_user/update_status",
        data: $(this).serialize(),
        success: function (response) {
          if (response.success == 'deactivated') {
            console.log(response)
            $(".confirmClose").click()
            $("#user-table").load(window.location.href + " #user-table") // load the user table with new data
            $("#alert_box h5").text("Deactivated Successfully");
            $("#alert_box").removeAttr('class');
            $("#alert_box").attr('class', 'alert alert-danger shadow-lg border d-flex align-items-center');    
            $("#alert_box").css('top', '5%'); // show the alert box        

              // alert will be hidden after 4 seconds
            setTimeout(function () {
              $("#alert_box").css('top', '-10%');
              location.reload();
            }, 2000);
          } else {
            console.log(response)
            $(".confirmClose").click()
            $("#user-table").load(window.location.href + " #user-table") // load the user table with new data
            $("#alert_box h5").text("Activated Successfully");
            $("#alert_box").removeAttr('class');
            $("#alert_box").attr('class', 'alert alert-primary shadow-lg border d-flex align-items-center');    
            $("#alert_box").css('top', '5%'); // show the alert box        

              // alert will be hidden after 4 seconds
            setTimeout(function () {
              $("#alert_box").css('top', '-10%');
              location.reload();
            }, 2000);
            }
        }
      });

    });
    // force submit
    $("#status_submit").click();

  }

  // when act button is clicked
  $("#activateUser").on('click', function () { 
    updateStatus();
  });
  // when deact button is clicked
  $("#deactivateUser").on('click', function () { 
    updateStatus();
  });
  
});



