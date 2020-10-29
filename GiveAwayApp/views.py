from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from GiveAwayApp.models import Donation, Institution


class LandingPageView(View):

    def get(self, request):
        donations = Donation.objects.count()
        institutions = Institution.objects.count()
        return render(request, 'index.html', {'donations': donations,
                                              'institutions': institutions})


class AddDonationView(TemplateView):
    template_name = 'form.html'


class LoginView(TemplateView):
    template_name = 'login.html'


class RegisterView(TemplateView):
    template_name = 'register.html'

# utwórz 4 proste widoki:
#
#     LandingPage
#
#     AddDonation
#
#     Login
#
#     Register
#     niech każdy obsługuje tylko metodę get i renderuje odpowiedni szablon html
#
