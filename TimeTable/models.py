from django.db import models
import os

# Create your models here.
class Timing(models.Model):
    start_time = models.TimeField(null = False)
    end_time = models.TimeField(null = True)

    def __str__(self):
        return self.start_time.strftime("%H:%M:%S") + " - " + self.end_time.strftime("%H:%M:%S")

class TimeTable(models.Model):

    DAYS_OF_WEEK = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
)

    day = models.CharField(max_length=9, choices=DAYS_OF_WEEK, null = False)
    timing = models.ForeignKey(Timing, on_delete=models.RESTRICT)
    subject = models.CharField(max_length=255, null = False)
    class_image = models.ImageField(upload_to='Class_Images')
    record_class = models.BooleanField(default=False)
    save_screenshot = models.BooleanField(default=False)

    def __str__(self):
        return "On " + self.day + " Join " + self.subject + " class starting from " + str(self.timing.start_time) + " till " + str(self.timing.end_time) + " {record class is set to " +  str(self.record_class) + " and save screenshot of class is set to " + str(self.save_screenshot) + " file path of image is '" + str(self.class_image)  + str(self.class_image) + "'}"