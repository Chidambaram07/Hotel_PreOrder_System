$(document).ready(function () {
    $('#log_email').on('input',function (e) { 
        var emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
        var email=$(this).val();
        if(!emailPattern.test(email)){
            $('#log_msg').html("Invalid Email format!");
        }else{
            $('#log_msg').html("");
        }
    });
    $('#reg_name').on('input', function () {
        var nameptn=/^[A-Za-z]{3,}$/;

        var name=$(this).val();
        if(nameptn.test(name)){
            $('#err_name').html("");
        }else{
            $('#err_name').html("Username should contain minimum 3 characters and no numbers!");
        }
    });
    $('#reg_email').on('input',function (e) { 
        var emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
        var email=$(this).val();
        if(!emailPattern.test(email)){
            $('#err_email').html("Invalid Email format!");
        }else{
            $('#err_email').html("");
        }
    });
    $('#reg_pwd').on('input', function () {
        var pwdptn=/^(?=.*\d)[A-Za-z\d]{6,}$/;
        var pwd=$(this).val();
        if(pwdptn.test(pwd)){
            $('#err_pwd').html("");
        }else{
            $('#err_pwd').html("Password should contain minimum 6 characters with numbers!");
        }
    });
});