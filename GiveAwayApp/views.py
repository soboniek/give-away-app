import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView, CreateView

from GiveAwayApp.forms import RegisterForm, LoginForm
from GiveAwayApp.models import Donation, Institution, Category


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


class AddDonationView(LoginRequiredMixin, View):

    def get(self, request):
        all_categories = Category.objects.all()
        all_institutions = Institution.objects.all()
        return render(request, 'form.html', {'all_categories': all_categories,
                                             'all_institution': all_institutions})

    def post(self, request):
        all_categories = Category.objects.all()
        all_institutions = Institution.objects.all()

        try:
            quantity = int(request.POST.get('bags'))
        except ValueError:
            msg = 'Wpisz poprawną ilość worków.'
            return render(request, 'form.html', {'all_categories': all_categories,
                                                 'all_institution': all_institutions,
                                                 'msg': msg})

        try:
            phone_number = int(request.POST.get('phone'))
        except ValueError:
            msg = 'Wpisz poprawny numer telefonu.'
            return render(request, 'form.html', {'all_categories': all_categories,
                                                 'all_institution': all_institutions,
                                                 'msg': msg})

        try:
            zip_code = int(request.POST.get('postcode'))
        except ValueError:
            msg = 'Wpisz poprawny kod pocztowy.'
            return render(request, 'form.html', {'all_categories': all_categories,
                                                 'all_institution': all_institutions,
                                                 'msg': msg})

        pick_up_date = request.POST.get('data')
        date_format = '%Y-%m-%d'
        try:
            datetime.datetime.strptime(pick_up_date, date_format)
        except ValueError:
            msg = 'Wybierz poprawną datę.'
            return render(request, 'form.html', {'all_categories': all_categories,
                                                 'all_institution': all_institutions,
                                                 'msg': msg})

        pick_up_time = request.POST.get('time')
        time_format = '%H:%M'
        try:
            datetime.datetime.strptime(pick_up_time, time_format)
        except ValueError:
            msg = 'Wybierz poprawną godzinę.'
            return render(request, 'form.html', {'all_categories': all_categories,
                                                 'all_institution': all_institutions,
                                                 'msg': msg})

        address = request.POST.get('address')
        city = request.POST.get('city')
        pick_up_comment = request.POST.get('more_info')
        institution_id = request.POST.get('organization')
        user_id = User.objects.get(id=self.request.user.id).id

        Donation.objects.create(quantity=quantity, address=address, phone_number=phone_number, city=city,
                                zip_code=zip_code, pick_up_date=pick_up_date, pick_up_time=pick_up_time,
                                pick_up_comment=pick_up_comment, institution_id=institution_id, user_id=user_id)

        return redirect('confirm-donation')


class ConfirmDonationView(TemplateView):
    template_name = 'form-confirmation.html'


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