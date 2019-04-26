 $(document).ready(function(){
     $('#button_validate_signup').click(function(){
        if ((validate_selects() == true) && (validate_email() == true) && (validate_phone_pin() == true) && (validate_name_username() == true) && (validate_dob_and_address() == true) && (validate_password() == true)){
            $.ajax({
                type:'post',
                url:$SCRIPT_ROOT + '/_user_signup',
                data:$('#signup_form').serialize(),
                dataType:'json',
                success:function(response){
                    if (response.status == "OK"){
                        window.location.href = "/";
                    }else if (response.status == "ERROR"){
                        location.reload();
                    }
                },
                error:function(response){
                  console.log("Error ! Try again after a while.");
                }
          });
        }
    });
});
//
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
    if ($("#city").val() == ""){
        no_invalids = false;
        $('#city-invalid-select').show();
        $('#city-invalid-select').text('Enter your city name');
    }else{
        $("#city-invalid-select").hide();
    }
    if ($("#state").val() == "Select a state"){
        no_invalids = false;
        $('#state-invalid-select').show();
    }else{
        $("#state-invalid-select").hide();
    }
    return no_invalids;
}

function validate_email(){
    var valid_email = true;
    email_id = $('#email').val()
    var email_regex = /^([a-zA-Z0-9_\.\-\+])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;

    if (email_id == ""){
        valid_email = false;
        $('#email-invalid-select').show();
        $('#email-invalid-select').text("Email ID cannot be empty");
    } else if(!email_regex.test(email_id)){
        $('#email-invalid-select').show();
        $('#email-invalid-select').text("Enter a valid email id");
    }else{
        $.ajax({
            type:'get',
            url:$SCRIPT_ROOT + '/_check_email_duplicate',
            data:{
                email: email_id
            },
            dataType:'json',
            success:function(response){
                if (response.status != "OK"){
                    valid_email = false;
                    $('#email-invalid-select').show();
                    $('#email-invalid-select').text("An account exists with this email id");
                }else{
                    valid_email = true;
                    $('#email-invalid-select').hide();
                }
            },
            error:function(){
                console.log("Error! there is some error");
                valid_email = false;
            }
        });
    }
    return valid_email;
}

function validate_phone_pin(){
    var valid_phone_pin = true;
    var phone_number = $('#phone').val();
    var location_pin = $('#pin').val();

    if (phone_number == ""){
        valid_phone_pin = false;
        $('#phone-invalid-select').show();
        $('#phone-invalid-select').text("Phone number cannot be empty");
    }else if (phone_number.length != 10){
        $('#phone-invalid-select').show();
        $('#phone-invalid-select').text("Invalid phone number");
    }else{
        $.ajax({
            type:'get',
            url:$SCRIPT_ROOT + '/_check_phone_duplicate',
            data:{
                phone: phone_number
            },
            dataType:'json',
            success:function(response){
                if (response.status != "OK"){
                    valid_phone_pin = false;
                    $('#phone-invalid-select').show();
                    $('#phone-invalid-select').text("Phone number already in use.");
                }else{
                    valid_phone_pin = true;
                    $('#phone-invalid-select').hide();
                }
            },
            error:function(){
                console.log("Error! there is some error");
                valid_phone_pin = false;
            }
        });
    }

    if (location_pin == ""){
        valid_phone_pin = false;
        $('#pin-invalid-select').show();
        $('#pin-invalid-select').text("PIN cannot be empty");
    }else if (location_pin.length != 6){
        valid_phone_pin = false;
        $('#pin-invalid-select').show();
        $('#pin-invalid-select').text("Invalid PIN");
    }else{
        $('#pin-invalid-select').hide();
    }
    return valid_phone_pin;
}


function validate_name_username(){
    var valid_name_user_name = true;
    var fname = $('#fname').val();
    var sname = $('#sname').val();
    var uname = $('#uname').val();

    if (fname == ""){
        valid_name_user_name = false;
        $('#fname-invalid-select').show();
        $('#fname-invalid-select').text("Enter first name");
    }else if (/\d/.test(fname)){
        valid_name_user_name = false;
        $('#fname-invalid-select').show();
        $('#fname-invalid-select').text("Invalid name");
    }else{
        $('#fname-invalid-select').hide();
    }

    if (/\d/.test(sname)){
        valid_name_user_name = false;
        $('#sname-invalid-select').show();
        $('#sname-invalid-select').text("Invalid name");
    }else{
        $('#sname-invalid-select').hide();
    }

    if (uname == ""){
        valid_name_user_name = false;
        $('#uname-invalid-select').show();
        $('#uname-invalid-select').text("Enter first name");
    }else if (uname.length < 5){
        $('#uname-invalid-select').show();
        $('#uname-invalid-select').text("UserName should be 7 characters or more");
    }else{
        $.ajax({
            type:'get',
            url:$SCRIPT_ROOT + '/_check_uname_duplicate',
            data:{
                user_name: uname
            },
            dataType:'json',
            success:function(response){
                if (response.status != "OK"){
                    valid_name_user_name = false;
                    $('#unmae-invalid-select').show();
                    $('#uname-invalid-select').text("Username Exists");
                }else{
                    valid_name_user_name = true;
                    $('#uname-invalid-select').hide();
                }
            },
            error:function(){
                console.log("Error! there is some error");
                valid_name_user_name = false;
            }
        });
    }
    return valid_name_user_name;
}

function validate_dob_and_address(){
    var valid_dob_address = true;
    var dob = $('#dob').val();
    var house_apt = $('#street_apt').val();

    if (house_apt == ""){
        valid_dob_address = false;
        $('#streetapt-invalid-select').show();
        $('#streetapt-invalid-select').text("House / Apt No. cannot be empty");
    }else{
        $('#streetapt-invalid-select').hide();
    }

    if (dob == ""){
        valid_dob_address = false;
        $('#dob-invalid-select').show();
        $('#dob-invalid-select').text("Select your D.O.B");
    }else{
        $('#dob-invalid-select').hide();
    }
    return valid_dob_address;
}

function validate_password(){
    var valid_password = true;
    var pass1 = $("#pass").val();
    var pass2 = $("#rpass").val();

    if (pass1 == ""){
        valid_password = false;
        $('#pass-invalid-select').show();
        $('#pass-invalid-select').text("Enter a password");
    }else if (pass1.length < 5){
        valid_password = false;
        $('#pass-invalid-select').show();
        $('#pass-invalid-select').text("Password too short");
    }else{
        $('#pass-invalid-select').hide();
    }

    if (pass2 == ""){
        valid_password = false;
        $('#rpass-invalid-select').show();
        $('#rpass-invalid-select').text("Re-Enter the password");
    }else{
        $('#pass-invalid-select').hide();
    }

    if(pass1 != pass2){
        valid_password = false;
        $('#pass-invalid-select').show();
        $('#rpass-invalid-select').text("Entered passwords do not match");
    }
    return valid_password;
}