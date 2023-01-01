from django.contrib import admin

# Register your models here.
from TimeTable.models import *

admin.site.register(Timing)
admin.site.register(TimeTable)
