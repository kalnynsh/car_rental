from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = ''