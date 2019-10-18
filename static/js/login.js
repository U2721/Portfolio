function openLogin() {
    document.getElementById('logimg').style.display = 'block';
    document.getElementById('loginBox').style.visibility = 'visible';
}

function openRegister() {
    document.getElementById('logimg').style.display = 'block';
    document.getElementById('RegisterBox').style.visibility = 'visible';
}

function closeLogin() {
    document.getElementById('logimg').style.display = 'none';
    document.getElementById('loginBox').style.visibility = 'hidden';
}

function closeRegister() {
    document.getElementById('logimg').style.display = 'none';
    document.getElementById('RegisterBox').style.visibility = 'hidden';
}

function loginSubmit() {
    console.log("!!!");
    var username = document.getElementById('LogUserName').value;
    var password = document.getElementById('LogPassword').value;
    console.log("登录用户名" + username + "密码" + password);
    /////别忘了从数据库中核对一下
}

function registerSubmit() {
    console.log("!!!");
    var username = document.getElementById('RegUsername').value;
    var password = document.getElementById('RegPassword').value;

    var radioValue;
    var radios = document.getElementsByName('user_type');
    for (var i = 0; i < radios.length; i++) {
        if (radios[i].checked == true) {
            radioValue = radios[i].value;
        }
    }
    console.log("注册用户名" + username + "密码" + password + "身份" + radioValue);

}
