# Sing Up
post => http://127.0.0.1:8000/api/account/sing-up/
required field: 

    {
        "username":"mossaddak",
        "email":"10000mossaddak@gmail.com",
        "password":"1234",
        "first_name":"Mossaddak",
        "last_name":"Hossain"
    }

# Accoutn Verification
post => http://127.0.0.1:8000/api/account/verify/
required field:
{
    "otp":"12279"
}


# Profile Picture

post, get, delete, patch => http://127.0.0.1:8000/api/profile-picture/

required field: img

Note: Authentication Mandetory