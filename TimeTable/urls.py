from django.urls import path
from . import views

urlpatterns = [
    path('', views.timetable, name = 'timetable'),
    path('edit_timings', views.edit_timings, name = 'edit_timings'),
    path('edit_subjects', views.edit_subjects, name = 'edit_subjects'),
    path('edit_timetable', views.edit_timetable, name = 'edit_timetable'),
]