from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def edit_timetable(request):

    entries_in_time = Timing.objects.all()
    entries_in_time_table = TimeTable.objects.all()
    timings = TimeTable.objects.values_list('timing')

    if entries_in_time:
        if entries_in_time_table:
            return render(request, "edit_timetable.html", {
                "time_table": entries_in_time_table,
                "timings": timings
                })

        else:
            return render(request, "edit_timetable.html", {"message": "Timing are added its time to make the time table."})
    else:
        return render(request, "edit_timetable.html", {"message": "Start by creating class timings."})

def edit_timing(request):
    return render(request, "edit_timetable.html")
