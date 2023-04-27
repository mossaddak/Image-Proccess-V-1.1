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

required field: input(form data)

# PDF to image
post => http://127.0.0.1:8000/api/app/pdf-proccess/
required field