import datetime
from random import randint

from django.contrib.auth.models import User
from faker import Faker
import pytest
from django.test import Client

from GiveAwayApp.models import Category, Donation, Institution

faker = Faker()


@pytest.fixture
def client():
    client = Client()
    return client


@pytest.fixture
def user():
    user = User.objects.create_user(username='aaa', password='aaa')
    user.save()
    return user


@pytest.fixture
def categories():
    for i in range(5):
        Category.objects.create(name=f"Name {i}")
    return Category.objects.all()


# @pytest.fixture
# def category():
#     category = Category.objects.create(name=f"Name category")
#     return category


@pytest.fixture
def donations(institutions, user):
    for i in range(5):
        Donation.objects.create(quantity=randint(1, 10),
                                institution=institutions[randint(0, 4)],
                                address=f'Address {i}',
                                phone_number=randint(100000000, 999999999),
                                city=f'City {i}',
                                zip_code=randint(10000, 99999),
                                pick_up_date=datetime.datetime.today() + datetime.timedelta(days=randint(1, 20)),
                                pick_up_time=f'{randint(1, 23)}:{randint(1, 59)}',
                                pick_up_comment=f'Comment {i}',
                                user=user)
    return Donation.objects.all()


# @pytest.fixture
# def donation(institutions):
#     donation = Donation.objects.create(quantity=randint(1, 10),
#                                        institution=institutions[randint(0, 4)],
#                                        address=f'Address',
#                                        phone_number=randint(100000000, 999999999),
#                                        city=f'City',
#                                        zip_code=randint(10000, 99999),
#                                        pick_up_date=datetime.datetime.today() + datetime.timedelta(days=randint(1, 20)),
#                                        pick_up_time=f'{randint(1, 23)}:{randint(1, 59)}',
#                                        pick_up_comment=f'Comment',
#                                        user=user)
#     return donation


@pytest.fixture
def institutions():
    for i in range(5):
        Institution.objects.create(name=f'Name {i}',
                                   description=f'Description {i}',
                                   type=randint(1, 3))
    return Institution.objects.all()
