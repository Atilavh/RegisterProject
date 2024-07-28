let $ = document
let get = function(id){return $.getElementById(id)}
let getC = function(className){return $.querySelector("."+className)}

const loginForm = getC('login-form')
const registerForm = getC('register-form')
const emailForm = getC('email-form')
const ChangePasswordForm = getC('change-pass-form')


function hideAllForms(){
    loginForm.classList.add("hidden")
    registerForm.classList.add("hidden")
    emailForm.classList.add("hidden")
    ChangePasswordForm.classList.add("hidden")
}
function showLoginForm(){
    loginForm.classList.remove("hidden")
}
function showregisterForm(){
    registerForm.classList.remove("hidden")
}
function showemailFormForm(){
    emailForm.classList.remove("hidden")
}
function showChangePasswordForm(){
    ChangePasswordForm.classList.remove("hidden")
}