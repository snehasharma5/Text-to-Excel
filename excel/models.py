from django.db import models


class File(models.Model):
    title = models.CharField(max_length=200, blank=True)
    excelFile = models.FileField(blank=True, upload_to='excelFile')

    def __str__(self):
        return self.title


class FileData(models.Model):
    email_id = models.EmailField()
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=20)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=200)
    ZIP = models.IntegerField(default=None)
    mobile = models.FloatField(default=None)
    date_of_birth = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name

# Create your models here.
