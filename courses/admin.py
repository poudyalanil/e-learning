from django.contrib import admin
from .models import Module, Unit, Lesson, Video, Quiz, Material

model_names = [Module, Unit, Lesson, Video, Quiz, Material]
admin.site.register(model_names)
