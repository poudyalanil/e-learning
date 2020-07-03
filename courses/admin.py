from django.contrib import admin
from .models import Module, Unit, Lesson, Video

model_names = [Module, Unit, Lesson, Video]
admin.site.register(model_names)
