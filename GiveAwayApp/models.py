from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)


class Institution(models.Model):
    INSTITUTION_CHOICES = [
        (1, 'Fundacja'),
        (2, 'Organizacja pozarządowa'),
        (3, 'Zbiórka lokalna')
    ]
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=80)
    type = models.IntegerField(choices=INSTITUTION_CHOICES,
                               default=1)
    categories = models.ManyToManyField(Category)


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution,
                                    on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=100)
    zip_code = models.IntegerField()
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.CharField(max_length=500)
    user = models.ForeignKey(User,
                             null=True,
                             default=True,
                             on_delete=models.CASCADE)
