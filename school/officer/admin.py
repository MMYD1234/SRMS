from django.contrib import admin
from .models import Student, Course, Grade, Teacher
# Register your models here.
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Grade)
admin.site.register(Teacher)