from django.shortcuts import render
from django.http import HttpResponse
from .models import Video, Lesson, Unit, Module


def index(requests):
    modules = Module.objects.all()

    return render(requests, "courses/index.html", {"courses": modules})


def single_course(requests, course_id):
    modules = Module.objects.get(pk=course_id)
    return render(requests, "courses/single_course.html", {"course": modules})
