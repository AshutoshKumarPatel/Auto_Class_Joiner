from django.contrib import admin

# Register your models here.
from TimeTable.models import *

admin.site.register(Timing)
admin.site.register(Monday)
admin.site.register(Tuesday)
admin.site.register(Wednesday)
admin.site.register(Thursday)
admin.site.register(Friday)
admin.site.register(Saturday)
admin.site.register(Sunday)
