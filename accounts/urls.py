from django.urls import path
from .views import SignUpView
from .views import UserSignUp, UserSignIn, change_password, show_user_profile, update_user, add_delete_cart, \
    add_delete_wishlist, user_wishlist, user_cart, PlaceOrder, change_order_status

urlpatterns = [
    path('accounts/', SignUpView.as_view(), name='signup'),
    path('signup/', UserSignUp.as_view()),
    path('signin/', UserSignIn.as_view()),
    path('userprofile/', show_user_profile.as_view()),
    path('update_user/', update_user.as_view()),
    path('change_password/', change_password.as_view()),
    path('add_delete_to_wishlist/', add_delete_wishlist.as_view()),
    path('add_delete_to_cart/', add_delete_cart.as_view()),
    path('user_wishlist/', user_wishlist.as_view()),
    path('user_cart/', user_cart.as_view()),
    path('place_order/', PlaceOrder.as_view()),
    path('change_status/', change_order_status.as_view())
]
