from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def timetable(request):

    entries_in_time = Timing.objects.all().order_by('start_time')
    entries_in_subject = Subject.objects.all().order_by('name')
    monday = Monday.objects.all()
    tuesday = Tuesday.objects.all()
    wednesday = Wednesday.objects.all()
    thursday = Thursday.objects.all()
    friday = Friday.objects.all()
    saturday = Saturday.objects.all()
    sunday = Sunday.objects.all()

    if entries_in_time:
        if entries_in_subject:
            if monday or tuesday or wednesday or thursday or friday or saturday or sunday:
                return render(request, "timetable.html", {
                    "timings": entries_in_time,
                    "monday": monday,
                    "tuesday": tuesday,
                    "wednesday": wednesday,
                    "thursday": thursday,
                    "friday": friday,
                    "saturday": saturday,
                    "sunday": sunday
                    })
            else:
                return render(request, "timetable.html", {"message": "Its time to make the time table.", "link" : "edit_timetable"})
        else:
            return render(request, "timetable.html", {"message" : "Its time to add Subjects.", "link" : "edit_subjects"})
    else:
        return render(request, "timetable.html", {"message": "Start by creating class timings.", "link" : "edit_timings"})

def edit_timings(request):
    return render(request, "edit_timings.html")

def edit_subjects(request):
    return render(request, "edit_subjects.html")

def edit_timetable(request):
    return render(request, "edit_timetable.html")


    
