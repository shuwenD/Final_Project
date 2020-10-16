from django.urls import path
from . import views
app_name = 'squirrel'

urlpatterns = [
	path('', views.map, name='map'),
]
