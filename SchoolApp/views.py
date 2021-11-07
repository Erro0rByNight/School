from django.views.generic import ListView
from .models import Class


# Create your views here.
class HomeListView(ListView):
	model = Class