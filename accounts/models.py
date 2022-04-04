from django.db import models
import uuid
from books.models import Book
from enum import Enum


# Create your models here.

class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]


class OrderStatus(ChoiceEnum):
    RECEIVED = "RECEIVED"
    PROGRESS = "PROGRESS"
    SHIPPED = "SHIPPED"
    DELIVERED = "DELIVERED"


class User(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, null=False)
    name = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=20, null=False)
    phone = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=500, null=True)
    is_deleted = models.BooleanField(null=True, default=True)
    is_admin = models.BooleanField(null=True, default=False)


class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    is_deleted = models.BooleanField(default=True, null=False)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    quantity = models.FloatField(default=0, null=False)
    is_deleted = models.BooleanField(default=True, null=False)


class Orders(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, null=False)
    product = models.ForeignKey(Book, max_length=200, null=True, blank=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=None)
    status = models.CharField(choices=OrderStatus.choices(), default=OrderStatus.RECEIVED.value, max_length=64)

    def __str__(self):
        return self.product.title
