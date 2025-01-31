from django.urls import path
from . import views
app_name = 'squirrel'

urlpatterns = [
	path('sightings/', views.list, name='list'),
        path('map', views.map, name = 'map'),
        path('sightings/add', views.add, name = 'add'),
        path('sightings/<str:sight_id>/', views.update, name = 'update'),
        path('sightings/stats', views.stat, name = 'stats'),
            ]
