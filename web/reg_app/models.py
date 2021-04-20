from django.db import models
from django.contrib.auth.models import User

User._meta.get_field('email')._unique = True

# Create your models here.

class Profile(models.Model): # make the attributes human readable as these names will be shown in the form fields
    
    RoleTypes = (
        ("STUDENT", "Student"),
        ("TEACHER", "Teacher"),
    )

    role = models.CharField(max_length=50, choices=RoleTypes)
    college = models.CharField(max_length=500)
    id_number = models.CharField(max_length=500)
    user = models.OneToOneField(User, on_delete=models.CASCADE) # we can do user.profile and profile.user on objects of User and Profile classes (one-to-one mapping)! if user is deleted, delete its profile.
    
    def __str__(self):
        return f'profile of {self.user.username}'



class StudentManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super(StudentManager, self).get_queryset(*args, **kwargs).filter(role='STUDENT') # return only the objects whose role is 'STUDENT'


class TeacherManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super(TeacherManager, self).get_queryset(*args, **kwargs).filter(role='TEACHER') # return only the objects whose role is 'TEACHER'



class StudentProfile(Profile): # a proxy for the Profile model 
    objects = StudentManager() # get the objects through filtering by role in StudentManager
    class Meta:
        proxy = True


class TeacherProfile(Profile): # a proxy for the Profile model 
    objects = TeacherManager() # get the objects through filtering by role in TeacherManager
    class Meta:
        proxy = True



