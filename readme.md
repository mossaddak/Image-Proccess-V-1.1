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

# Account Verification
-)First:
    need to hit this url, user must need loged in:
    post => http://127.0.0.1:8000/api/account/account-verify-code/

-)Second:
    then you have to hit the below link with the otp you got through the email 
    post => http://127.0.0.1:8000/api/account/verify/
    required field:
        {
            "otp":"12279"
        }

# Login
post => http://127.0.0.1:8000/api/account/login/

required fields:
    {
        "username":"mossaddak1",
        "password":"1234"
    }

# Profile Picture

post, get, delete, patch => http://127.0.0.1:8000/api/profile-picture/

required field: img
Note: Authentication Mandetory

# Profile 
post, patch => http://127.0.0.1:8000/api/account/profile/

required fields:
    {
        "id": 16,
        "username": "mossaddak1",
        "first_name": "Mossaddak",
        "last_name": "",
        "email": "10000mossaddak1@gmail.com"
    }

Note: Here have to pass "username" field for patching

# Image Procesing
post => http://127.0.0.1:8000/api/app/image-proccess/
get => http://127.0.0.1:8000/api/app/image-proccess/<id>/

required field: input(form data)
note: only super admin has permission of GET

# PDF to image
post => http://127.0.0.1:8000/api/app/pdf-proccess/
get => http://127.0.0.1:8000/api/app/pdf-proccess/<id>/

required field: input(form data)
note: only super admin has permission of GET

# Password Required
post => http://127.0.0.1:8000/api/reset-password/

required field:
    {
        "email":"10000mossaddak1@gmail.com"
    }

# Reset password send token
post => http://127.0.0.1:8000/api/reset-password/

required field:
    {
        "password_reset_token":<here will be the token send by email>,
        "new_password":12345
    }