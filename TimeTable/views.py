from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def edit_timetable(request):

    entries_in_time = Timing.objects.all().order_by('start_time')
    monday = Monday.objects.all()
    tuesday = Tuesday.objects.all()
    wednesday = Wednesday.objects.all()
    thursday = Thursday.objects.all()
    friday = Friday.objects.all()
    saturday = Saturday.objects.all()
    sunday = Sunday.objects.all()

    if entries_in_time:
        if monday or tuesday or wednesday or thursday or friday or saturday or sunday:
            return render(request, "edit_timetable.html", {
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
            return render(request, "edit_timetable.html", {"message": "Timing are added its time to make the time table."})
    else:
        return render(request, "edit_timetable.html", {"message": "Start by creating class timings."})

def edit_timing(request):
    return render(request, "edit_timetable.html")
