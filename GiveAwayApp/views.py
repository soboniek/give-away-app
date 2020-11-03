from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView

from GiveAwayApp.forms import RegisterForm, LoginForm
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


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('landing-page')

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
        try:
            login(self.request, user)
        except AttributeError:
            return redirect('register')
        return super().form_valid(form)


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = User.objects.create_user(form.cleaned_data['email'],
                                        form.cleaned_data['email'],
                                        form.cleaned_data['password1'])
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.save()
        return super().form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('landing-page')