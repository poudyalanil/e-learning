from django.db import models
from django_countries.fields import CountryField

# Model Hierarchy
# Users
#     |_Enrolled Courses


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20)
    highest_education = models.CharField(max_length=20)
    interest = models.CharField(max_length=20)
    country = CountryField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    bio = models.TextField()

    def __str__(self):
        return (self.first_name, self.last_name, self.email, self.bio)


class Enroll(models.Model):
    pass
