from django.db import models

# Create your models here.
class Student(models.Model):
    gender_choices=(
        ('male', 'Male'),
        ('female', 'Female'),
    )

    grade_choices = (
        ('one', '1'),
        ('two', '2'),
        ('three', '3'),
        ('four', '4'),
        ('five', '5'),
        ('six', '6'),
        ('seven', '7'),
        ('eight', '8'),
        ('nine', '9'),
        ('ten', '10'),
        ('eleven', '11'),
        ('twelve', '12'),
    )
    
    section_choices = (
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
        ('d', 'D'),
    )


    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, help_text='optional', null=True, blank=True)
    last_name = models.CharField(max_length=20)
    phone_number = models.IntegerField()
    gender = models.CharField(max_length=5, choices=gender_choices)
    date_of_birth = models.DateField(help_text='yyyy/mm/dd')
    address = models.TextField(max_length=150)
    grade = models.CharField(max_length=15, choices= grade_choices)
    section = models.CharField(max_length=5, choices= section_choices)

    def __str__(self):
        return self.first_name

