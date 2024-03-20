from django.shortcuts import render
from django.views.generic import ListView

from .models import Student, Teacher


def students_list(request):
    template = "school/students_list.html"
    student = Student.objects.all().prefetch_related('teachers')
    context = {
        "object_list": student
    }
    ordering = "group"
    return render(request, template, context)
