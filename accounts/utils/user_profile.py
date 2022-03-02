from ..models import User, WishList, Cart
from rest_framework import status
from books.models import Book


def userProfile(data):
    pid = data.get('uid')
    user_profile_object = User.objects.filter(uid=pid).first()
    result = {}
    if user_profile_object:
        result['name'] = user_profile_object.name
        result['address'] = user_profile_object.address
        result['phone'] = user_profile_object.phone
        result['email'] = user_profile_object.email
        result['result'] = 'SUCCESS'
        result['status'] = status.HTTP_200_OK
    else:
        result = {'result': 'USER_NOT_FOUND', 'status': status.HTTP_400_BAD_REQUEST}
    return result


def update_user_profile(user_uid, name, phone, address):
    user_obj = User.objects.filter(uid=user_uid).first()
    if user_obj:
        user_obj.name = name
        user_obj.phone = phone
        user_obj.address = address
        user_obj.save()
        result = {"result": "USER_DATA_SUCCESSFULLY_UPDATED", "status": status.HTTP_200_OK}
    else:
        result = {"result": "USER_NOT_FOUND", "status": status.HTTP_200_OK}
    return result


def change_user_password(user_uid, previous_password, new_password):
    user_obj = User.objects.filter(uid=user_uid).first()
    if user_obj and user_obj.password == previous_password:
        user_obj.password = new_password
        user_obj.save()
        result = {'result': "PASSWORD_CHANGED_SUCCESSFULLY", "status": status.HTTP_200_OK}
    else:
        result = {'result': "USER_NOT_FOUND", "status": status.HTTP_200_OK}
    return result


def add_delete_to_wishlist(user, product, add=False):
    previous_wishlist_obj = WishList.objects.filter(user=user, product=product).first()
    if add:
        if previous_wishlist_obj:
            previous_wishlist_obj.is_deleted = False
            previous_wishlist_obj.save()
            return "PREVIOUS_OBJECT_MARKED_FALSE_SUCCESSFULLY"
        else:
            wishlist_obj = WishList(user=user, product=product, is_deleted=False)
            wishlist_obj.save()
            return "NEW_OBJECT_CREATED_SUCCESSFULLY"
    else:
        if previous_wishlist_obj:
            previous_wishlist_obj.is_deleted = True
            previous_wishlist_obj.save()
            return "OBJECT_DELETED_SUCCESSFULLY"
        else:
            return "NO_OBJECT_FOUND_CAN'T_DELETE"


def add_delete_to_cart(user, product, quantity, add=False):
    previous_cart_obj = Cart.objects.filter(user=user, product=product).first()
    if add:
        if previous_cart_obj:
            previous_cart_obj.is_deleted = False
            previous_cart_obj.quantity = quantity
            previous_cart_obj.save()
            return "PREVIOUS_OBJECT_MARKED_FALSE_SUCCESSFULLY"
        else:
            cart_obj = Cart(user=user, product=product, quantity=quantity, is_deleted=False)
            cart_obj.save()
            return "NEW_OBJECT_CREATED_SUCCESSFULLY"
    else:
        if previous_cart_obj:
            previous_cart_obj.is_deleted = True
            previous_cart_obj.save()
            return "OBJECT_DELETED_SUCCESSFULLY"
        else:
            return "NO_OBJECT_FOUND_CAN'T_DELETE"
