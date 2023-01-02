from django.db import models
import os

# Create your models here.
class Timing(models.Model):
    start_time = models.TimeField(null = False)
    end_time = models.TimeField(null = True)

    def __str__(self):
        return self.start_time.strftime("%H:%M:%S") + " - " + self.end_time.strftime("%H:%M:%S")

class Monday(models.Model):

    timing = models.OneToOneField(Timing, on_delete=models.RESTRICT, primary_key= True)
    subject = models.CharField(max_length=255, null = False)
    class_image = models.ImageField(upload_to='Class_Images')
    record_class = models.BooleanField(default=False)
    save_screenshot = models.BooleanField(default=False)

    def __str__(self):
        return "On Monday" + " Join " + self.subject + " class starting from " + str(self.timing.start_time) + " till " + str(self.timing.end_time) + " {record class is set to " +  str(self.record_class) + " and save screenshot of class is set to " + str(self.save_screenshot) + " file path of image is '" + str(self.class_image)  + str(self.class_image) + "'}"
        
class Tuesday(models.Model):

    timing = models.OneToOneField(Timing, on_delete=models.RESTRICT, primary_key= True)
    subject = models.CharField(max_length=255, null = False)
    class_image = models.ImageField(upload_to='Class_Images')
    record_class = models.BooleanField(default=False)
    save_screenshot = models.BooleanField(default=False)

    def __str__(self):
        return "On Tuesday" + " Join " + self.subject + " class starting from " + str(self.timing.start_time) + " till " + str(self.timing.end_time) + " {record class is set to " +  str(self.record_class) + " and save screenshot of class is set to " + str(self.save_screenshot) + " file path of image is '" + str(self.class_image)  + str(self.class_image) + "'}"

class Wednesday(models.Model):

    timing = models.OneToOneField(Timing, on_delete=models.RESTRICT, primary_key= True)
    subject = models.CharField(max_length=255, null = False)
    class_image = models.ImageField(upload_to='Class_Images')
    record_class = models.BooleanField(default=False)
    save_screenshot = models.BooleanField(default=False)

    def __str__(self):
        return "On Wednesday" + " Join " + self.subject + " class starting from " + str(self.timing.start_time) + " till " + str(self.timing.end_time) + " {record class is set to " +  str(self.record_class) + " and save screenshot of class is set to " + str(self.save_screenshot) + " file path of image is '" + str(self.class_image)  + str(self.class_image) + "'}"

class Thursday(models.Model):

    timing = models.OneToOneField(Timing, on_delete=models.RESTRICT, primary_key= True)
    subject = models.CharField(max_length=255, null = False)
    class_image = models.ImageField(upload_to='Class_Images')
    record_class = models.BooleanField(default=False)
    save_screenshot = models.BooleanField(default=False)

    def __str__(self):
        return "On Thrusday" + " Join " + self.subject + " class starting from " + str(self.timing.start_time) + " till " + str(self.timing.end_time) + " {record class is set to " +  str(self.record_class) + " and save screenshot of class is set to " + str(self.save_screenshot) + " file path of image is '" + str(self.class_image)  + str(self.class_image) + "'}"
        
class Friday(models.Model):

    timing = models.OneToOneField(Timing, on_delete=models.RESTRICT, primary_key= True)
    subject = models.CharField(max_length=255, null = False)
    class_image = models.ImageField(upload_to='Class_Images')
    record_class = models.BooleanField(default=False)
    save_screenshot = models.BooleanField(default=False)

    def __str__(self):
        return "On Friday" + " Join " + self.subject + " class starting from " + str(self.timing.start_time) + " till " + str(self.timing.end_time) + " {record class is set to " +  str(self.record_class) + " and save screenshot of class is set to " + str(self.save_screenshot) + " file path of image is '" + str(self.class_image)  + str(self.class_image) + "'}"

class Saturday(models.Model):

    timing = models.OneToOneField(Timing, on_delete=models.RESTRICT, primary_key= True)
    subject = models.CharField(max_length=255, null = False)
    class_image = models.ImageField(upload_to='Class_Images')
    record_class = models.BooleanField(default=False)
    save_screenshot = models.BooleanField(default=False)

    def __str__(self):
        return "On Saturday" + " Join " + self.subject + " class starting from " + str(self.timing.start_time) + " till " + str(self.timing.end_time) + " {record class is set to " +  str(self.record_class) + " and save screenshot of class is set to " + str(self.save_screenshot) + " file path of image is '" + str(self.class_image)  + str(self.class_image) + "'}"

class Sunday(models.Model):

    timing = models.OneToOneField(Timing, on_delete=models.RESTRICT, primary_key= True)
    subject = models.CharField(max_length=255, null = False)
    class_image = models.ImageField(upload_to='Class_Images')
    record_class = models.BooleanField(default=False)
    save_screenshot = models.BooleanField(default=False)

    def __str__(self):
        return "On Sunday" + " Join " + self.subject + " class starting from " + str(self.timing.start_time) + " till " + str(self.timing.end_time) + " {record class is set to " +  str(self.record_class) + " and save screenshot of class is set to " + str(self.save_screenshot) + " file path of image is '" + str(self.class_image)  + str(self.class_image) + "'}"
