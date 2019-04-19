 $(document).ready(function(){
 alert("working");
     $('#signup-form').submit(function(){
     alert("working");
        if (validate_form() == true){
            return true;
         }else{
            return false;
         }
    });
});

function validate_form(){
    var is_valid_form = true;
    if (validate_selects() != true){
        is_valid_form = false;
    }
    if (validate_inputs() != true){
        is_valid_form = false;
    }
    return is_valid_form;
 }

 function validate_selects(){
        var no_invalids = true;

        if ($("#account_type").val() == "none"){
            no_invalids = false;
            $('#account-type-invalid').show();
        }else{
            $('#account-type-invalid').hide();
        }
        if ($("#gender").val() == "none"){
            no_invalids = false;
            $('#gender-invalid-select').show();
        }else{
            $("#gender-invalid-select").hide();
        }
        if ($("#district").val() == "none"){
            no_invalids = false;
            $('#district-invalid-select').show();
        }else{
            $("#district-invalid-select").hide();
        }
        if ($("#city").val() == "none"){
            no_invalids = false;
            $('#city-invalid-select').show();
        }else{
            $("#city-invalid-select").hide();
        }
        if ($("#state").val() == "none"){
            no_invalids = false;
            $('#state-invalid-select').show();
        }else{
            $("#state-invalid-select").hide();
        }
        return no_invalids;
 }

 function validate_inputs(){
    var no_invalids = true;
   if (validate_email() == false){
        no_invalids = false;
        $('#email-invalid-select').show();
        $('#email-invalid-select').text("Account exists with this email");
    }else{
        $('#email-invalid-select').hide();
    }
    return no_invalids;
 }

 function validate_email(){
    alert("validating email");
    $.ajax({
        type:'get',
        url:'http://theshadowfashion.com/check_email_duplicate',
        data:{
            "email": $('#email').val(),
        },
        dataType:'json',
        success:function(response){
            if (response.status != "OK"){
                alert("validation success");
                $('#email-invalid-select').show();
                $('#email-invalid-select').text("An account exists with this email");
            }else{
                alert("validation failed");
                //$('#invalid_credentials').show();
            }
        },
        error:function(){
          alert("Error!");
        }
  });
 }
