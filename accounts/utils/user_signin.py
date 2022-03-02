from ..models import User
from rest_framework import status


def userSignIn(data):
    result = {}
    phone = data.get('phone')
    email = data.get('email')
    password = data.get('password')
    if email:
        user_object = User.objects.filter(email=email).first()
    else:
        user_object = User.objects.filter(phone=phone).first()
    if user_object:
        if user_object.password == password:
            result['result'] = 'SUCCESS'
            result['uid'] = user_object.uid
            result['user_name'] = user_object.name
            result['status'] = status.HTTP_200_OK
        else:
            result['result'] = "PASSWORD_MATCH_FAILED"
            result['uid'] = None
            result['user_name'] = None
            result['status'] = status.HTTP_400_BAD_REQUEST
    else:
        result['result'] = "FAILED_USER_NOT_EXIST"
        result['status'] = status.HTTP_400_BAD_REQUEST

    return result
