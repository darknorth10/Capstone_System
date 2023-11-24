
// Dashboard Top Selling Graph
$(document).ready(function () {

  var top1 = $("#top1");
  var top2 = $("#top2");
  var top3 = $("#top3");


  const data = {
    labels: [
      top1.attr("data-name"),
      top2.attr("data-name"),
      top3.attr("data-name")
    ],
    datasets: [{
      label: 'Transactions',
      data: [top1.attr("data-count"), top2.attr("data-count"), top3.attr("data-count")],
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

    options: {
      layout: {
          padding: 20
      }
  }
  });

  const myModal = new mdb.Modal(document.getElementById('dashboardModal'), {})
  myModal.toggle()




});

// document is ready and loaded
$(document).ready(function() {

  //dashboard stock level
    // stock level
    var prod1 = $("#prod1");
    var prod2 = $("#prod2");
    var prod3 = $("#prod3");
    var prod4 = $("#prod4");
    var prod5 = $("#prod5");

    // change color and level of stocks

    //prod1
   var prod1stock = (parseInt(prod1.attr('data-stock')) / parseInt(prod1.attr('data-max'))) * 100;
   var pgcolor;

   if(prod1stock >= 75) {
    pgcolor = "bg-primary";
    $("#stocklabel1").text('Good');

   } else if(prod1stock < 75 && prod1stock > 30 ) {
    pgcolor = "bg-success";
    $("#stocklabel1").text('Normal');

   } else if(prod1stock <= 30 && prod1stock > 15 ) {
    pgcolor = "bg-warning";
    $("#stocklabel1").text('Warning');

   } else if(prod1stock <= 15 && prod1stock > 0 ) {
    pgcolor = "bg-danger";
    $("#stocklabel1").text('Critical');

   } else if(prod1stock == 0) {
    pgcolor = "bg-secondary";
    $("#stocklabel1").text('Out of Stock');

   }
   $("#product1stock").css('width', `${prod1stock}%`);
   $("#product1stock").attr('class', `progress-bar ${pgcolor}`);

   // product 2
   var prod2stock = (parseInt(prod2.attr('data-stock')) / parseInt(prod2.attr('data-max'))) * 100;
   var pgcolor2;

   if(prod2stock >= 75) {
    pgcolor2 = "bg-primary";
    $("#stocklabel2").text('Good');
   } else if(prod2stock < 75 && prod2stock > 30 ) {
    pgcolor2 = "bg-success";
    $("#stocklabel2").text('Normal');
   } else if(prod2stock <= 30 && prod2stock > 15 ) {
    pgcolor2 = "bg-warning";
    $("#stocklabel2").text('Warning');
   } else if(prod2stock <= 15 && prod2stock > 0 ) {
    pgcolor2 = "bg-danger";
    $("#stocklabel2").text('Critical');
   } else if(prod2stock == 0) {
    pgcolor2 = "bg-secondary";
    $("#stocklabel2").text('Out of Stock');
   }

    $("#product2stock").css('width', `${prod2stock}%`);
    $("#product2stock").attr('class', `progress-bar ${pgcolor2}`);

   // product 3
   var prod3stock = (parseInt(prod3.attr('data-stock')) / parseInt(prod3.attr('data-max'))) * 100;
   var pgcolor3;

   if(prod3stock >= 75) {
    pgcolor3 = "bg-primary";
    $("#stocklabel3").text('Good');

   } else if(prod3stock < 75 && prod3stock > 30 ) {
    pgcolor3 = "bg-success";
    $("#stocklabel3").text('Normal');

   } else if(prod3stock <= 30 && prod3stock > 15 ) {
    pgcolor3 = "bg-warning";
    $("#stocklabel3").text('Warning');

   } else if(prod3stock <= 15 && prod3stock > 0 ) {
    pgcolor3 = "bg-danger";
    $("#stocklabel3").text('Critical');

   } else if (prod3stock == 0){
    pgcolor3 = "bg-secondary";
    $("#stocklabel3").text('Out of Stock');

   }

    $("#product3stock").css('width', `${prod3stock}%`);
    $("#product3stock").attr('class', `progress-bar ${pgcolor3}`);


   // product 4
   var prod4stock = (parseInt(prod4.attr('data-stock')) / parseInt(prod4.attr('data-max'))) * 100;
   var pgcolor4;

   if(prod4stock >= 75) {
    pgcolor4 = "bg-primary";
    $("#stocklabel4").text('Good');

   } else if(prod4stock < 75 && prod4stock > 30 ) {
    pgcolor4 = "bg-success";
    $("#stocklabel4").text('Normal');

   } else if(prod4stock <= 30 && prod4stock > 15 ) {
    pgcolor4 = "bg-warning";
    $("#stocklabel4").text('Warning');

   } else if(prod4stock <= 15 && prod4stock > 0 ) {
    pgcolor4 = "bg-danger";
    $("#stocklabel4").text('Critical');

   } else {
    pgcolor4 = "bg-secondary";
    $("#stocklabel4").text('Out of Stock');
    console.log(prod4stock)
   }

    $("#product4stock").css('width', `${prod4stock}%`);
    $("#product4stock").attr('class', `progress-bar ${pgcolor4}`);

   // product 5
   var prod5stock = (parseInt(prod5.attr('data-stock')) / parseInt(prod5.attr('data-max'))) * 100;
   var pgcolor5;

   if(prod5stock >= 75) {
    pgcolor5 = "bg-primary";
    $("#stocklabel5").text('Good');

   } else if(prod5stock < 75 && prod5stock > 30 ) {
    pgcolor5 = "bg-success";
    $("#stocklabel5").text('Normal');

   } else if(prod5stock <= 30 && prod5stock > 15 ) {
    pgcolor5 = "bg-warning";
    $("#stocklabel5").text('Warning');

   } else if(prod5stock <= 15 && prod5stock > 0 ) {
    pgcolor5 = "bg-danger";
    $("#stocklabel5").text('Critical');

   } else if(prod5stock == 0) {
    pgcolor5 = "bg-secondary";
    $("#stocklabel5").text('Out of Stock');

   }

    $("#product5stock").css('width', `${prod5stock}%`);
    $("#product5stock").attr('class', `progress-bar ${pgcolor5}`);









  // side nav
  var shrink = false;

  $('#shrink').click(function() {

    if (shrink == true) {
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
      $('.text-label h2:last-of-type').css('font-size', '1.1em')
      shrink = false;
    } else {
      $('.sidenav').css('width', "18%");
      setTimeout(function() {
        $('.sidenav-menu li span').show();
      }, 500);
      $('.sidenav-menu li i').css("font-size", "0.7rem");
      $('.sidenav').css('justify-content', "flex-start");
      $('#navlogo').css('visibility', 'visible');
      // $('#navlogo').css('visibility', 'visible');
      $('#navlogo').show()
      //$('.sidenav-menu').css('gap', '15px');
      $('#shrink').css('transform', 'rotate(0deg)');
      $('.left-symbol').css('width', '20%')
      $('.text-label h2:last-of-type').css('font-size', '1em')
      shrink = true;

    }

  });




  // Alert Function
  $(document).ready(function () {
    if ( $("#alert_box h5").text() != "" ) {
      $("#alert_box").css('top', '3%'); // show the alert box

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

  $(".posform input").attr("class", "form-control text-center w-75 p-2 bg-white shadow-inner");
  $(".posform input").attr("min", '1');


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


  // Product management

  // add product form attribute

  $('#id_product_name').attr('class', 'form-control');
  $('#id_product_name').attr('maxlength', '40');
  $('#id_brand').attr('class', 'form-control');
  $('#id_brand').attr('maxlength', '40');
  $('#id_product_size').attr('class', 'role-select rounded');
  $('#id_category').attr('class', 'role-select rounded');
  $('#id_price').attr('class', 'form-control');
  $('#id_current_stock').attr('class', 'form-control');
  $('#id_max_stock').attr('class', 'form-control');
  $('#id_availability').attr('class', 'form-check-input');
  $('#id_product_img').attr('class', 'form-control');


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

 // shows current stock in add stock form
  $("#id_current_stock").change(function () {
    $("#curr_stock").text($(this).val())
  });
// submits add stock form on confirm
  $("#conf_addStock").click(function () {
    $("#addstock_form").submit();
  });


  // Customer Profile

  $("#regcust").click(function () {

    $("#add_cust_submit").click();
  });

  // POS

  // clicking items will ask for quantity
  $(document).on("click", ".itemwrapper .item", function () {
    var x = $(this).parent().attr("data-productname");
    var y = $(this).parent().attr("data-productid");
    var z = $(this).parent().attr("data-currentstock");

    $(".conf_quantity_pos").text(x);
    $('#id_product_id').val(y);


    $('#id_quantity').val('1');
    $('#curr_stock').text(z);
    $('#quantity_conf').removeAttr('disabled');

    $("#pos_quantity_trigger").click();

  });

  // clear the pos transaction

  $('#clearbtn').click(function () {

    $('#clearpos').submit();

  });

   // desired quantity must be less than the number of currrent stocks else  btn is disabled
   $("#id_quantity").change(function (e) {
    var currentStock = parseInt($("#curr_stock").text());

    if ($(this).val() <= currentStock) {
      $('#quantity_conf').removeAttr('disabled');

    } else {
      $('#quantity_conf').attr('disabled', 'disabled');
    }
  });

  // increase or decrese quantity pos
  $('.dcr').click(function () {
    var currentStock = parseInt($("#curr_stock").text());

    if ($(".posform input[type=number]").val() > 1) {

        $(".posform input[type=number]").val(parseInt($(".posform input[type=number]").val()) - 1)
    }

     // disable confirm button when desired quantity exceeded current stocks
     if ($(".posform input[type=number]").val() <= currentStock) {
      $('#quantity_conf').removeAttr('disabled');

    } else {
      $('#quantity_conf').attr('disabled', 'disabled');
    }

  });

  $('.incr').click(function () {
    var currentStock = parseInt($("#curr_stock").text());

   $(".posform input[type=number]").val(parseInt($(".posform input[type=number]").val()) + 1);

    // disable confirm button when desired quantity exceeded current stocks
    if ($(".posform input[type=number]").val() <= currentStock) {
      $('#quantity_conf').removeAttr('disabled');

    } else {
      $('#quantity_conf').attr('disabled', 'disabled');
    }

  });



  //  item search shadow on focus
  $('.positemsearch').focus(function () {
    $('.pos_search').css('outline', '2px solid rgb(68,168,236)');
    console.log('test')
  });
  $('.positemsearch').blur(function () {
    $('.pos_search').css('outline', '0');
    console.log('test')
  });


   // Disable proceed button when mop was not selected
   $('#pos_proceed').attr('disabled', 'disabled');

   // downpayment value
   var downpayment = parseFloat($('#subtotal').attr('data-subtotal')) * .3;


   // for selecting mode of payment
  $('.mop_div div input[name="mop"]').change(function () {
    console.log($(this).val())

    // enables proceed button
    $('#pos_proceed').removeAttr('disabled');


    //  Mode of payment forms hide and show
    switch ($(this).val()) {
      case 'cash':
        $('.mop_div div').css('outline', '1px solid rgb(145, 145, 145)')
        $('.mop_div div h5').css('color', '#eee')
        $(this).parent().css("outline", '2px solid rgb(124, 166, 213)');
        $(this).siblings('h5').css("color", 'rgb(124, 166, 213)');

        $('#id_transaction_type').val('Cash');
        var total_amt = parseFloat($('#subtotal').attr('data-subtotal'))
        $('#id_total_price').val(total_amt);
        $('#id_status').val('Complete');

        var dp = downpayment.toLocaleString('en-PH', {currency: 'PHP', style: 'currency'});
        console.log(dp);
        $('.dp').text('');
        $('.pos_downpayment').text(dp);

        $('#cash_form').show(0);
        $('#gcash_form').hide(0);
        $('#banking_form').hide(0);
        break;

      case 'gcash':
        $('.mop_div div').css('outline', '1px solid rgb(145, 145, 145)')
        $('.mop_div div h5').css('color', '#eee')
        $(this).parent().css("outline", '2px solid rgb(124, 166, 213)');
        $(this).siblings('h5').css("color", 'rgb(124, 166, 213)');

        $('#gcash_transaction_type').val('Gcash');
        var total_amt = parseFloat($('#subtotal').attr('data-subtotal'))
        $('#gcash_total_price').val(total_amt);
        $('#gcash_status').val('Complete');

        var dp = downpayment.toLocaleString('en-PH', {currency: 'PHP', style: 'currency'});
        console.log(dp);
        $('.dp').text('');
        $('.pos_downpayment').text(dp);

        $('#cash_form').hide(0);
        $('#banking_form').hide(0);
        $('#gcash_form').show(0);
        break;


      case 'banking':
        $('.mop_div div').css('outline', '1px solid rgb(145, 145, 145)')
        $('.mop_div div h5').css('color', '#eee')
        $(this).parent().css("outline", '2px solid rgb(124, 166, 213)');
        $(this).siblings('h5').css("color", 'rgb(124, 166, 213)');

        $('#bank_transaction_type').val('Banking');
        var total_amt = parseFloat($('#subtotal').attr('data-subtotal'))
        $('#bank_total_price').val(total_amt);

        var dp = downpayment.toLocaleString('en-PH', {currency: 'PHP', style: 'currency'});
        console.log(dp);
        $('.dp').text('');
        $('.pos_downpayment').text(dp);

        $('#cash_form').hide(0);
        $('#banking_form').show(0);
        $('#gcash_form').hide(0);
        break;

      default:
        break;
    }
  });

  //  Installment Switch
 var toggelInstallment = false;
 $('.downpayment').hide();


 $("#installmentswitch").change(function() {

     if (toggelInstallment) {
      // Cash
       $(".downpayment").hide();
       $(".changecash").show();
       $('#id_installment').val("false");
       $('#gcash_installment').val("false");
       $('#bank_installment').val("false");
       toggelInstallment = false;

       $('#id_customer_name').removeAttr('required');
       $('#id_contact').removeAttr('required');
       $('#id_email').removeAttr('required');
       $('#id_delivery_address').removeAttr('required');

       $('#gcash_customer_name').removeAttr('required');
       $('#gcash_contact').removeAttr('required');
       $('#gcash_email').removeAttr('required');
       $('#gcash_delivery_address').removeAttr('required');



     } else {
      // Cash
       $(".downpayment").show(0);
       $(".changecash").hide(0);
       $('#id_installment').val("true");
       $('#gcash_installment').val("true");
       $('#bank_installment').val("true");
       toggelInstallment = true;

       $('#id_customer_name').attr('required', 'required');
       $('#id_contact').attr('required', 'required');
       $('#id_email').attr('required', 'required');
       $('#id_delivery_address').attr('required', 'required');

       $('#gcash_customer_name').attr('required', 'required');
       $('#gcash_contact').attr('required', 'required');
       $('#gcash_email').attr('required', 'required');
       $('#gcash_delivery_address').attr('required', 'required');
     }

 });

  //  Change cash on change event

  // compute change on change event FOR CASH MOP
 $('#id_amount').keyup(function () {
    if(!toggelInstallment) {
      if ($(this).val() >= parseFloat($('#subtotal').attr('data-subtotal')) ) {

        var a = $(this).val() - parseFloat($('#subtotal').attr('data-subtotal'));
        $(this).attr('data-value', a);

        change = a.toLocaleString('en-PH', {currency: 'PHP', style: 'currency'});
        $('.x').text('');
        $('#pos_change').text(change);
        $('.conf_transaction').removeAttr('disabled');

        $('#id_change').val(a);

      }
      else {
        var a = 0
        $('.x').text('');
        phcurrency = a.toLocaleString('en-PH', {currency: 'PHP', style: 'currency'});
        $('#pos_change').text(phcurrency.toString());
        $('.conf_transaction').attr('disabled', 'disabled');
        $('#id_change').val(a);
      }
    }
    // if installment is toggled
    else {

      if ($(this).val() >= downpayment) {

        var b = 0.00
        var change = b;

        $('.conf_transaction').removeAttr('disabled');
        $('#id_change').val(b);
        $('.conf_transaction').removeAttr('disabled');
      }
      else {
        var a = 0
        $('.dp').text('');
        phcurrency = a.toLocaleString('en-PH', {currency: 'PHP', style: 'currency'});
        $('#pos_change').text(phcurrency.toString());
        $('.conf_transaction').attr('disabled', 'disabled');
        $('#id_change').val(a);
      }
    }
 });

   // keyup event FOR GCASH MOP to add transaction
   $('#gcash_amount').keyup(function () {
      if(!toggelInstallment) {

        if ($(this).val() == parseFloat($('#subtotal').attr('data-subtotal'))) {

          $('.conf_transaction').removeAttr('disabled');

        }
        else {
          $('.conf_transaction').attr('disabled', 'disabled');
        }

        // if Installment Banking mop
    } else {
        if($(this).val() >= downpayment) {
          $('.conf_transaction').removeAttr('disabled');
        } else {
          $('.conf_transaction').attr('disabled', 'disabled');
        }
    }
 });


   // keyup event FOR bank MOP to add transaction
  $('#bank_amount').keyup(function () {
    // if not installment and banking mop
      if(!toggelInstallment) {

        if ($(this).val() == parseFloat($('#subtotal').attr('data-subtotal'))) {

          $('.conf_transaction').removeAttr('disabled');

        }
        else {
          $('.conf_transaction').attr('disabled', 'disabled');
        }

        // if Installment Banking mop
     } else {
        if($(this).val() >= downpayment) {
          $('.conf_transaction').removeAttr('disabled');
        } else {
          $('.conf_transaction').attr('disabled', 'disabled');
        }
     }
  });



 // adds class for form fields in cash form
 $('#id_customer_name').attr('class', 'form-control');
 $('#id_contact').attr('class', 'form-control');
 $('#id_email').attr('class', 'form-control');
 $('#id_delivery_address').attr('class', 'form-control');
 $('#id_amount').attr('class', 'form-control');
 $('#id_amount').attr('step', '1');
 $('#id_amount').attr('min', '0');



 // show receipt or detailed view in transaction

    // onlick to change hidden traansaction no. value and  trigger modal to pop up
 $('.parentReceiptBtn').on('click', '.receiptbtn', function () {
    var trasaction_no = $(this).attr('data-transnumber');
    console.log(trasaction_no);

    $("#trans_no_modal").text(trasaction_no);
        // loads the content of detailed table
    $('#detailed_div').load(window.location.href + trasaction_no + '/ #detailed_div')
        // shows modal
    $("#trigger3").click()

 });


  // INSTALLMENT BALANCCE TRANSACTION

  $("#trans_reference").change(function (e) {

    var selectedOption = $('option:selected', this);

    var cname = selectedOption.attr('data-cname');
    var total_amount = selectedOption.attr('data-total');
    var paid_amount = selectedOption.attr('data-paid');
    var due_date = selectedOption.attr('data-due');
    var balance = parseFloat(total_amount) - parseFloat(paid_amount);

    if ($(this).val() == "") {
      $("#balance").text("");
      $("#balance_cname").text("");
      $("#balance_due").text("");
      $("#balance_transaction_reference").val($(this).val());
      $("#balance_customer_name").val("");
    } else {
      console.log(due_date);

      $("#balance").text(balance.toLocaleString('en-PH', {currency: 'PHP', style: 'currency'}));
      $("#balance_cname").text(cname);
      $("#balance_due").text(due_date);
      $("#balance_transaction_reference").val($(this).val());
      $("#balance_customer_name").val(cname);
    }



  });
  $("#balance_transaction_reference").val($("#trans_reference").val());

  // hide or show he referrence no in pay balance form depending on the payment method
  $("#balance_payment_method").change(function (e) {
    if( $(this).val() == "Cash") {
        $("#balance_refno").hide(0);
        $("#balance_reference_no").removeAttr('required');
    } else if( $(this).val() == "Gcash" || $(this).val() == "Banking") {
        $("#balance_refno").show(0);
        $("#balance_reference_no").attr('required', 'required');
    } else {
         $("#balance_refno").hide(0);
         $("#balance_reference_no").removeAttr('required');
    }
  });


  // sort items by name or category POS through ajax call

  $("input[name='searchItemName']").change(function (e) {
    var itemName = $(this).val();

      $("#itemNameSearch").val(itemName);

      // submit everytime search name input value changes
      $("#searchItemForm").submit()


  });

  $("#searchItemForm").submit(function (e) {
    e.preventDefault();

    $.ajax({
      type: "POST",
      url: window.location.href + "search_items/",
      data: $(this).serialize(),
      success: function (response) {
        console.log(response.success);
        location.reload();
      }
    });

  });



  // Void Product
  $(document).on('click', '.voidbtn', function () {
    var itemName = $(this).attr('data-voidProd');

    console.log(itemName);
    $("#curr_prod").text(itemName);
    $("input[name='voidName']").val(itemName);
    $("#voidTrigger").click();
  });


  $('select[name="itemName"]').change(function (e) {
      console.log('test')

      var optSelected = $('option:selected', this);

      $("#return_name").val($(this).val());
      $("#return_orig_quantity").val(optSelected.attr('data-quantity')) ;
      $("#return_size").val(optSelected.attr('data-size'));
      $("#return_transact_no").val(optSelected.attr('data-tnum'));


  });


  var notifShow = false;

  // $("#notif-btn").css('display', 'block');
  $("#notif-btn").click(function (e) {
    e.preventDefault();

    if(!notifShow) {
      notifShow = true;
      $("#notif_content").css('display', 'block');
    } else {
      notifShow = false;
      $("#notif_content").css('display', 'none');
    }

  });

  $("#notifclose").click(function (e) {
    e.preventDefault();
    notifShow = false;
    $("#notif_content").css('display', 'none');
  });

});



