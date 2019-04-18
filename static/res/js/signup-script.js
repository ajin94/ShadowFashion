 $(document).ready(function(){
     $('#button_validate_signup').click(function(){

        if (validate_form() == true){
            $.ajax({
               type:'post',
               url:$SCRIPT_ROOT + '/_user_signup',
               data:$('#signup-form').serialize(),
               dataType:'json',
               success:function(response){
                 if (response.status == "OK"){
                   location.reload();
                 }
                },
                error:function(){
                   alert("Error!");
                }
             });
         }
  });
});

 function validate_form(){
    var is_valid_form = true;
    if (validate_selects() != true){
    alert("validating selects");
        is_valid_form = false;
    }
    if (validate_inputs() != true){
    alert("validating inputs");
        is_valid_form = false;
    }
    return is_valid_form
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
    if ($("#email").val() == ""){
        $('#email-invalid-select').show();
        $('#email-invalid-select').text("Email cannot be empty");
        no_invalids = false;
    }else{
       if (validate_email($("#email").val()) == false){
            no_invalids = false;
            $('#email-invalid-select').show();
            $('#email-invalid-select').text("Enter a valid Email");
        }else{
            $('#email-type-select').hide();
        }
    }
    return no_invalids
 }

 function validate_email(email){
    var re = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/
    alert(email);
    var emailFormat = re.test(email);
    if (emailFormat == true) {
        alert("validation success");
        return true;
    }else{
        alert("validation failed");
        return false;
    }
 }
