from django.db import models
from datetime import date

# Model Hierarchy

# Courses
#     |_Modules
#         |_Units
#             |_Lessons
#                 |_Videos
#                 |_Quizes
#                 |_Materials


class Material(models.Model):
    material_title = models.CharField(max_length=50)


class Quiz(models.Model):
    quiz_title = models.CharField(max_length=20)


class Video(models.Model):
    video_title = models.CharField(max_length=50)
    video_length = models.CharField(max_length=20)
    today = date.today()
    date_published = today.strftime('%d/%m/%Y')


class Lesson(models.Model):
    lesson_title = models.CharField(max_length=50)
    lesson_description = models.TextField(default="Null")

    videos = models.ManyToManyField(Video)
    quizes = models.ManyToManyField(Quiz)
    materials = models.ManyToManyField(Material)


class Unit(models.Model):
    unit_title = models.CharField(max_length=50)
    unit_description = models.TextField(default="Null")

    lessons = models.ForeignKey(Lesson, on_delete=models.CASCADE)


class Module(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    today = date.today()
    last_update = today.strftime('%d/%m/%Y')
    units = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
