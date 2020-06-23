from django.db import models
from datetime import datetime

# Model Hierarchy

# Courses
#     |_Modules
#         |_Units
#             |_Lessons
#                 |_Videos
#                 |_Quizes
#                 |_Materials


class Module(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    last_update = datetime.now()

    def __str__(self):
        return (self.title, self.author, self.last_update)


class Unit(models.Model):
    pass


class Lesson(models.Model):
    pass


class Video(models.Model):
    pass


class Quiz(models.Model):
    pass


class Material(models.Model):
    pass
