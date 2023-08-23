from django.db import models

# Create your models here.

class Personal_info(models.Model):
    Choices = (
        ('1','Male'),
        ('2','Female'),
        ('3','other')
    )
    name = models.CharField(max_length=225)
    email = models.EmailField()
    contact = models.CharField(max_length=13)
    city = models.CharField(max_length=225)
    address = models.CharField(max_length=225)
    gender = models.CharField(max_length=2,choices=Choices)
    occupation = models.CharField(max_length=255)
    dob = models.DateField()
    pan_card = models.FileField()
    voter_id = models.FileField()
    profile_pic = models.ImageField(upload_to = "static")
    agree = models.BooleanField()
    # type = models.CharField(max_length=2,choices=Choices,null=True,blank=True)

    def __str__(self):
        return self.name
    
class Task(models.Model):
    Choices = (
        ('1','Complete'),
        ('2','In-process'),
        ('3','Hold'),
        ('4','Close')
    )
    Project = models.CharField(max_length=225)
    Task = models.CharField(max_length=225)
    work_in_progress = models.CharField(max_length=2,choices=Choices)
    start_date = models.DateField()
    end_date = models.DateField()
    

    def __str__(self):
        return self.Project
    

