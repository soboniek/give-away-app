"""GiveAway URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf import settings

from GiveAwayApp.views import LandingPageView, AddDonationView, LoginView, RegisterView, LogoutView, ConfirmDonationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='landing-page'),
    path('add_donation/', AddDonationView.as_view(), name='add-donation'),
    path('confirm_donation/', ConfirmDonationView.as_view(), name='confirm-donation'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout', LogoutView.as_view(), name='logout'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
