from django.db import models
import uuid
from books.models import Book


# Create your models here.

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
