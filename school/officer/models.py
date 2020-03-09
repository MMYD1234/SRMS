from django.db import models

# Create your models here.
class Student(models.Model):
    gender_choices=(
        ('male', 'Male'),
        ('female', 'Female'),
    )


    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, help_text='optional', null=True, blank=True)
    last_name = models.CharField(max_length=20)
    phone_number = models.IntegerField()
    gender = models.CharField(max_length=5, choices=gender_choices)
    date_of_birth = models.DateField(help_text='yyyy/mm/dd')
    address = models.TextField(max_length=150)
    

    def __str__(self):
        return self.first_name


class Grade(models.Model):

    grade = models.IntegerField()
    section = models.CharField(max_length=20)
    year = models.IntegerField()
     
    def __str__(self):
        return '{}{}'.format(self.grade, self.section)

class Course(models.Model):
    course_id = models.CharField(max_length=50, primary_key=True)
    course_name = models.CharField(max_length=50)
    grade_number = models.ForeignKey(Grade, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.course_name
    
class Teacher(models.Model):
    gender_choices=(
        ('male', 'Male'),
        ('female', 'Female'),
    )


    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, help_text='optional', null=True, blank=True)
    last_name = models.CharField(max_length=20)
    phone_number = models.IntegerField()
    gender = models.CharField(max_length=5, choices=gender_choices)
    date_of_birth = models.DateField(help_text='yyyy/mm/dd')
    address = models.TextField(max_length=150)
    

    def __str__(self):
        return self.first_name

class CourseGradeTeacher(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, default=1)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=1)