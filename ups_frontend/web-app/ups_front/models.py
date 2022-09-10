from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your models here.

class CreatedUsersForm(UserCreationForm):
    email = forms.EmailField(
        error_messages={'required': 'email should not be empty'})

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']


class Truck_info(models.Model):
    truck_id = models.IntegerField(primary_key=True)
    truck_status = models.CharField(max_length=32)


class Package_info(models.Model):
    package_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(
        User, related_name='user_package', null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=32)
    destination_x = models.IntegerField()
    destination_y = models.IntegerField()
    # which field in the foreign table
    truck = models.ForeignKey(
        Truck_info, related_name='truck_package', on_delete=models.CASCADE)


class Product_info(models.Model):
    product_id = models.IntegerField()
    description = models.CharField(max_length=64)
    count = models.IntegerField(default=0)
    package = models.ForeignKey(
        Package_info, related_name='package_product', on_delete=models.CASCADE)


class Feedback_info(models.Model):
    user = models.ForeignKey(
        User, related_name='user_feedback', on_delete=models.CASCADE)
    grade = models.IntegerField()
    text = models.CharField(max_length=500)
