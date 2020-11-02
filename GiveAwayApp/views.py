from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from GiveAwayApp.models import Donation, Institution


class LandingPageView(View):

    def get(self, request):
        donations_counter = Donation.objects.count()
        institutions_counter = Institution.objects.count()
        institutions_found = Institution.objects.filter(type=1)
        institutions_nongov_organization = Institution.objects.filter(type=2)
        institutions_local_collection = Institution.objects.filter(type=3)
        return render(request, 'index.html', {'donations_counter': donations_counter,
                                              'institutions_counter': institutions_counter,
                                              'institutions_found': institutions_found,
                                              'institutions_nongov_organization': institutions_nongov_organization,
                                              'institutions_local_collection': institutions_local_collection})


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
