from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import TemplateView

from frontend import Car
from frontend import Booking


class HomeView(TemplateView):
    template_name = 'frontend/home.html'

    def get_context_data(self, **kwargs):
        ctx = super(HomeView, self).get_context_data(**kwargs)

        cars = Car.objects.filter(is_available=True)
        ctx['cars'] = cars

        return ctx


class CarDetailsView(DetailView):
    template_name = 'frontend/car_details.html'
    model = Car

    def get_context_data(self, **kwargs):
        ctx = super(CarDetailsView, self).get_context_data(**kwargs)
        ctx['booking_success'] = 'booking-success' in self.request.GET

        return ctx



