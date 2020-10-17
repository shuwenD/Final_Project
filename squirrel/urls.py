from django.urls import path
from . import views
app_name = 'squirrel'

urlpatterns = [
	path('', views.list, name='list'),
        path('add', views.add, name = 'add'),
        path('<int:sight_id>', views.detail, name = 'detail'),# wrong, to be corrected
]
