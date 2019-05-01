 $(document).ready(function(){
     $('#send_message').click(function(){
         if (validate_message_fields() == true){
            $.ajax({
                type:'post',
                url:$SCRIPT_ROOT + '/_send_message',
                data:$('#message_form').serialize(),
                dataType:'json',
                success:function(response){
                    if (response.status == "OK"){
                        clear_fields();
                        // $('#message_send_modal').modal('show');
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

function validate_message_fields(){
    var customer_email = $('#c_email').val();
    var customer_message = $('#c_message').val();
    var email_valid = true;
    var email_regex = /^([a-zA-Z0-9_\.\-\+])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    if(!email_regex.test(customer_email)){
        email_valid = false;
        $('#email-type-invalid').show();
    }else{
        $('#email-type-invalid').hide();
    }
    if(customer_message == ""){
        email_valid = false;
        $('#message-type-invalid').show();
    }else{
        $('#message-type-invalid').hide();
    }
    return email_valid;
}

function clear_fields(){
    alert("resetting fields");
    $('#message_form')[0].reset();
}