from django.db import models

# Create your models here.


type_choices = (
    ('Class Activity','Class Activity'),
    ('Sports', 'Sports'),
    ('Club','Club'),
    ('Others','Others'),
)

class Event(models.Model):
    event_type = models.CharField(max_length=200, choices=type_choices, default='Class Activity')
    event_name = models.CharField(max_length=200)
    teacher = models.CharField(max_length=200)
    content = models.TextField()
    event_image = models.TextField()
    event_date = models.IntegerField()

    def __str__(self):
        return self.event_name

class ImportantDates(models.Model):
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.create_date.strftime("%m/%d/%Y %H:%M:%S")
