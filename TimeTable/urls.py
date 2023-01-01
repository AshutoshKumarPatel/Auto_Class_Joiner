from django.urls import path
from . import views

urlpatterns = [
    path('', views.edit_timetable, name = 'edit_timetable'),
    path('edit_timing', views.edit_timing, name = 'edit_timing')
]