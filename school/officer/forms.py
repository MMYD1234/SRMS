from django import forms
from .models import Student, Grade, Course, Teacher

class RegisterForm(forms.ModelForm):
    class Meta():
        model = Student
        fields = '__all__'

class RegisterTeacherForm(forms.ModelForm):
    class Meta():
        model = Teacher
        fields = '__all__'

class CreateGradeForm(forms.ModelForm):
    class Meta():
        model = Grade
        fields = '__all__'

class CreateCourseForm(forms.ModelForm):
    class Meta():
        model = Course
        fields = '__all__'