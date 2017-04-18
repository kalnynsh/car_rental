"""carrental URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from frontend.views import CarDetailsView
from frontend.views import NewBookingView
from frontend.views import HomeView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^car/(?P<pk>\d+)/$', CarDetailsView.as_view(), name='car-details'),

    url(r'^booking/(?P<car_pk>\d+)/$', NewBookingView.as_view(), name='new-booking'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

