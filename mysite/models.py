from django.db import models

# Create your models here.

#mysite_students

class students(models.Model):
    first=models.CharField(max_length=30)
    last=models.CharField(max_length=30)


    def __str__(self):
        return self.first


class contact(models.Model):
    email=models.EmailField()
    subject= models.CharField(max_length=196)
    message=models.TextField()

    def __str__(self):
        return self.email
