import datetime
from random import randint

from django.contrib.auth.models import User

from GiveAwayApp.models import Category, Donation, Institution


def create_users():
    User.objects.create_user('aaa', email='aaa@aaa.pl', password='aaa')
    User.objects.create_user('bbb', email='bbb@bbb.pl', password='bbb')
    User.objects.create_user('ccc', email='ccc@ccc.pl', password='ccc')


def create_categories():
    for i in range(5):
        Category.objects.create(name=f"Name {i}")


def create_donations():
    for i in range(5):
        Donation.objects.create(quantity=randint(1, 10),
                                institution=Institution.objects.get(pk=randint(0, 4)),
                                address=f'Address {i}',
                                phone_number=randint(100000000, 999999999),
                                city=f'City {i}',
                                zip_code=randint(10000, 99999),
                                pick_up_date=datetime.datetime.today() + datetime.timedelta(days=randint(1, 20)),
                                pick_up_time=f'{randint(1, 23)}:{randint(1, 59)}',
                                pick_up_comment=f'Comment {i}',
                                user=User.objects.all()[0])


def create_institutions():
    for i in range(5):
        Institution.objects.create(name=f'Name {i}',
                                   description=f'Description {i}',
                                   type=randint(1, 3))


def create_donation_categories():
    for i in range(1, 6):
        donation = Donation.objects.get(id=i)
        for j in range(3):
            cat = Category.objects.get(id=randint(1, 5))
            donation.categories.add(cat)


def create_institution_categories():
    for i in range(1, 6):
        institution = Institution.objects.get(id=i)
        for j in range(3):
            cat = Category.objects.get(id=randint(1, 5))
            institution.categories.add(cat)
