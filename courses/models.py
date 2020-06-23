from django.db import models

# Model Hierarchy

# Courses
#     |_Modules
#         |_Units
#             |_Lessons
#                 |_Videos
#                 |_Quizes
#                 |_Materials


class Module(models.Model):
    pass


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
