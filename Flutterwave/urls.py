"""Flutterwave URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Flutterwave.settings import MEDIA_ROOT, MEDIA_URL
from payment.views import make_payment, initiate_payment, verify_payment

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home, name='home'),
    path('make/', make_payment, name='payment',),
    path('', initiate_payment, name='initiate-payment'),
    path('<str:reference>', verify_payment, name='verify-payment')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
