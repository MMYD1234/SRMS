from django.db import models

# Create your models here.
class Teacher(models.Model):

    gender_choices=(
        ('male', 'Male'),
        ('female', 'Female'),
    )

    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, help_text='*optional', null=True, blank=True)
    last_name = models.CharField(max_length=20)
    phone_number = models.IntegerField()
    gender = models.CharField(max_length=5, choices=gender_choices)
    date_of_birth = models.DateField(help_text='yyyy/mm/dd')
    address = models.TextField(max_length=150)
    
    def __str__(self):
        return {}+{}.format(self.first_name,self.last_name)