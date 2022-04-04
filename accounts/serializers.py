from rest_framework import serializers
from .models import User
from books.models import Book
from accounts.models import OrderStatus, Orders


class UserSignUpRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'phone', 'address']


class UserSignInRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'phone', 'password']


class ChangePasswordSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(max_length=20, required=True, allow_null=False)
    uid = serializers.UUIDField(required=True)

    class Meta:
        model = User
        fields = ["uid", "password", "new_password"]


class UpdateUserSerializer(serializers.ModelSerializer):
    uid = serializers.UUIDField(required=True)

    class Meta:
        model = User
        fields = ["uid", "name", "phone", "address"]


class UserProfileSerializer(serializers.ModelSerializer):
    uid = serializers.UUIDField(required=True)

    class Meta:
        model = User
        fields = ["uid"]


class AddDeleteWishlistSerializer(serializers.Serializer):
    user = serializers.UUIDField(required=True)
    product = serializers.CharField(required=True, max_length=200)
    add = serializers.BooleanField(required=True)

    def validate_user(self, value):
        user_obj = User.objects.filter(uid=value).first()
        if user_obj:
            return user_obj
        return serializers.ValidationError("user not found")

    def validate_product(self, value):
        product_obj = Book.objects.filter(title=value).first()
        if product_obj:
            return product_obj
        return serializers.ValidationError("product not found")


class AddDeleteCartSerializer(serializers.Serializer):
    user = serializers.UUIDField(required=True)
    product = serializers.CharField(required=True, max_length=200)
    quantity = serializers.FloatField(required=True)
    add = serializers.BooleanField(required=True)

    def validate_user(self, value):
        user_obj = User.objects.filter(uid=value).first()
        if user_obj:
            return user_obj
        return serializers.ValidationError("user not found")

    def validate_product(self, value):
        product_obj = Book.objects.filter(title=value).first()
        if product_obj:
            return product_obj
        return serializers.ValidationError("product not found")


class UserWishlistSerializer(serializers.Serializer):
    user = serializers.UUIDField(required=True)

    def validate_user(self, value):
        user_obj = User.objects.filter(uid=value).first()
        if user_obj:
            return user_obj
        return serializers.ValidationError("user not found")


class UserOrderPlaceSerializer(serializers.Serializer):
    product = serializers.CharField(required=True, max_length=200)
    user = serializers.UUIDField(required=True)

    def validate_user(self, value):
        user_obj = User.objects.filter(uid=value).first()
        if user_obj:
            return user_obj
        return serializers.ValidationError("user not found")

    def validate_product(self, value):
        book_obj = Book.objects.filter(title=value).first()
        if book_obj:
            return book_obj
        return serializers.ValidationError("book not found")


class ChangeOrderStatusSerializer(serializers.Serializer):
    order = serializers.UUIDField(required=True)
    status = serializers.CharField(max_length=64, default=OrderStatus.RECEIVED.value)

    def validate_order(self, value):
        order_obj = Orders.objects.filter(uid=value).first()
        if order_obj:
            return order_obj
        return serializers.ValidationError("order not found")

    def validate_status(self, value):
        if value in [OrderStatus.RECEIVED.value, OrderStatus.PROGRESS.value, OrderStatus.SHIPPED.value,
                     OrderStatus.DELIVERED.value]:
            return value
        return serializers.ValidationError("status value is not correct")
