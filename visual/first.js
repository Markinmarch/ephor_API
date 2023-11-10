// coming soon
window.onload = addName;

function addName() {
    var buttonName = document.getElementById("addParams");
    buttonName.onclick = handleButtonClick;
}

function handleButtonClick() {
    var textInputName = document.getElementById("userName");
    var userName = textInputName.value;
    var textInputAge = document.getElementById("userAge");
    var userAge = textInputAge.value;
    if (userName == "" || userAge == "") {
        alert("Введите параметры, пожалуйста!");
    }
    else {
        alert("Ваше имя: " + userName + " Ваш возраст: " + userAge);
    }
}
